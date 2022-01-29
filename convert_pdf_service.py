import os

from slack_sdk import WebClient

from converter import Converter
from message import Message


class ConvertPdfService:
    def __init__(self):
        self.client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))

    def execute(self, event, say):
        channel = event["item"]["channel"]
        timestamp = event["item"]["ts"]

        group_history = self.get_threads(channel, timestamp)

        # json_to_Message
        messages = []
        for message in group_history.data["messages"]:
            messages.append(Message(message))

        file_name = Converter(messages).to_pdf()

        return self.client.files_upload(
            channels=channel,
            initial_comment="スレッドで要件定義はやめてくれ委員会会長",
            file=file_name
        )

    def get_threads(self, channel, timestamp):
        # timestampからメッセージ特定
        group_history = self.client.conversations_replies(channel=channel, ts=timestamp)
        messages = group_history.data["messages"]

        # スレッド元でない可能性を考慮し、再取得 TODO refactor
        timestamp = messages[0]["thread_ts"]
        return self.client.conversations_replies(channel=channel, ts=timestamp)
