import os

from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

from app import app

flask_app = Flask(__name__)

handler = SlackRequestHandler(app)


# Flask アプリへのルートを登録します
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)
