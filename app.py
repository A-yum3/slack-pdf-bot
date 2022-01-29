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
    emoji = event["reaction"]
    if emoji == "pdf":
        return ConvertPdfService().execute(event, say)
    return True
