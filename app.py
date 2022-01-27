import logging
import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk import WebClient

logging.basicConfig(level=logging.INFO)

client = WebClient(os.environ["SLACK_BOT_TOKEN"])

app = App()


@app.event("reaction_added")
def reaction_add(event, say):
    emoji = event["reaction"]
    user = event["user"]
    item_user = event["item_user"]
    channel = event["item"]["channel"]
    ts = event["item"]["ts"]

    if user == item_user:
        return

    # タイムスタンプでメッセージを特定
    conversations_history = client.conversations_history(
        channel=channel, oldest=ts, latest=ts, inclusive=1
    )

    messages = conversations_history.data["messages"]

    # メッセージが取得出来ない場合、スレッドからメッセージを特定
    if not messages:
        group_history = client.conversations_replies(channel=channel, ts=ts)
        messages = group_history.data["messages"]

    reactions = messages[0]["reactions"]

    target_reaction = os.environ["SLACK_REACTION_KEY"]
    start_postmessage = False

    reactions_text = ""

    for reaction in reactions:
        reactions_text += ":{}:{} ".format(reaction["name"], reaction["count"])
        if reaction["name"] == target_reaction:
            start_postmessage = True

    if not start_postmessage:
        return

    userslist = client.users_list()
    members = userslist["members"]

    for member in members:
        if member["id"] == user:
            reaction_user = member["real_name"]
            break

    response = client.chat_postEphemeral(
        channel=channel,
        user=item_user,
        text=f"{reaction_user} さんが以下のメッセージにリアクション :{emoji}: を追加しました\n\n"
             + messages[0]["text"]
             + f"\n{reactions_text}",
    )


from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=3000)
