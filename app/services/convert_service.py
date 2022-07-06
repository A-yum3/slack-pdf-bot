import os

from slack_sdk import WebClient
from slack_sdk.web.slack_response import SlackResponse

from app.factory.message_factory import MessageFactory
from app.infra.pdf_converter import PdfConverter


class ConvertService:
    def __init__(self):
        self.client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))

    def execute(self, event, say):
        """

        Args:
            event:
                {
                    "type": "reaction_added",
                    "user": "U024BE7LH",
                    "reaction": "thumbsup",
                    "item_user": "U0G9QF9C6",
                    "item": {
                        "type": "message",
                    "channel": "C0G9QF9GZ",
                    "ts": "1360782400.498405"
                    },
                    "event_ts": "1360782804.083113"
                }
            say:

        Returns:

        """
        channel = event["item"]["channel"]
        timestamp = event["item"]["ts"]

        group_history = self.get_threads(channel, timestamp)

        # TODO Refactor
        user_table = {}
        users = group_history.data['messages'][0]['reply_users']
        for user in users:
            response = self.client.users_info(user=user)
            user_table[user] = {
                'name': response.data['user']['real_name'],
                'image': response.data['user']['profile']['image_24']
            }

        # json_to_Message
        messages = [MessageFactory.create(message) for message in group_history.data["messages"]]

        file_name = PdfConverter(messages, user_table).execute()

        return self.client.files_upload(
            channels=channel,
            initial_comment="スレッドで要件定義はやめてくれ委員会会長",
            file=file_name
        )

    def get_threads(self, channel: str, timestamp: str) -> SlackResponse:
        """
        メッセージを指定し、元スレッドメッセージを取得する
        Args:
            channel: チャンネルID
            timestamp: 送信メッセージタイムスタンプ

        Returns:
            SlackResponse:
        """

        group_history = self.client.conversations_replies(channel=channel, ts=timestamp)
        messages = group_history.data["messages"]

        timestamp = messages[0]["thread_ts"]
        return self.client.conversations_replies(channel=channel, ts=timestamp)
