from models.message import Message


class MessageFactory:

    @classmethod
    def create(cls, message: dict) -> Message:
        return Message(message)
