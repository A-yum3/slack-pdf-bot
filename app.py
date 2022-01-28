import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk import WebClient

from converter import Converter

load_dotenv()  # debug

client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))

app = App(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    token=os.environ.get("SLACK_BOT_TOKEN")
)


# 絵文字が付けられたら付けられたスレッドを読む
@app.event('reaction_added')
def reaction_add(event, say):
    # response処理 TODO toFunction
    emoji = event["reaction"]
    if emoji != "pdf":
        return
    channel = event["item"]["channel"]
    ts = event["item"]["ts"]
    item_user = event["item_user"]

    # timestampからメッセージ特定
    group_history = client.conversations_replies(channel=channel, ts=ts)
    messages = group_history.data["messages"]

    # スレッド元でない可能性を考慮し、再取得 TODO refactor
    ts = messages[0]["thread_ts"]
    group_history = client.conversations_replies(channel=channel, ts=ts)
    messages = group_history.data["messages"]
    max_message_count = int(messages[0]["reply_count"])
    title = messages[0]["text"]

    output_messages = []
    for i in range(1, max_message_count + 1):  # 1-origin
        output_messages.append(messages[i]["text"])

    file_name = Converter(output_messages).to_pdf()

    client.files_upload(
        channels=channel,
        initial_comment="スレッドで要件定義はやめてくれ委員会会長",
        file=file_name
    )
