import json
import os

from slack_sdk import WebClient

from services.convert_service import ConvertService


class TestConvertPdfService(object):
    def test_execute(self, mocker):
        """
        reaction_addが行われた際に正常にプロセスが終了する

        :param mocker:
        :return:
        """

        with open('./dummies/conversations_replies_dummy.json', 'r') as f:
            conversations_replies_response = json.load(f)

        with open('./dummies/reaction_added.json', 'r') as f:
            event = json.load(f)

        dummy_slack_response = type("dummy", (object,), {
            "data": conversations_replies_response
        })

        mocker.patch.object(WebClient, 'files_upload', return_value=True)
        mocker.patch.object(WebClient, 'conversations_replies', return_value=dummy_slack_response)

        result = ConvertService().execute(event, None)
        assert result

        os.remove('output.pdf')
