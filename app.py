import os

from dotenv import load_dotenv
from slack_bolt import App

from convert_pdf_service import ConvertPdfService

load_dotenv()  # debug

app = App(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    token=os.environ.get("SLACK_BOT_TOKEN")
)


@app.event('reaction_added')
def reaction_add(event, say):
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
    emoji = event["reaction"]
    if emoji == "pdf":
        return ConvertPdfService().execute(event, say)
    return True
