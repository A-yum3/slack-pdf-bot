import os
from slack_bolt import App
from slack_sdk import WebClient

client = WebClient(os.environ["SLACK_BOT_TOKEN"])

app = App(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    token=os.environ.get("SLACK_BOT_TOKEN")
)


# 絵文字が付けられたら付けられたスレッドを読む
@app.event('reaction_added')
def reaction_add(event, say):
    emoji = event["reaction"]
    if emoji != "pdf":
        return
    channel = event["item"]["channel"]
    ts = event["item"]["ts"]
    item_user = event["item_user"]

    group_history = client.conversations_replies(channel=channel, ts=ts)
    messages = group_history.data["messages"]
    title = messages[0]["text"]
    max_message_count = int(messages[0]["reply_count"])

    output_messages = []
    for i in range(1, max_message_count):
        output_messages.append(messages[i]["text"])

    response_message = "\n".join(output_messages)

    client.chat_postEphemeral(
        channel=channel,
        user=item_user,
        text=response_message
    )


from flask import Flask, request

flask_app = Flask(__name__)

# SlackRequestHandler は WSGI のリクエストを Bolt のインターフェイスに合った形に変換します
# Bolt レスポンスからの WSGI レスポンスの作成も行います
from slack_bolt.adapter.flask import SlackRequestHandler

handler = SlackRequestHandler(app)


# Flask アプリへのルートを登録します
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    # handler はアプリのディスパッチメソッドを実行します
    return handler.handle(request)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)
