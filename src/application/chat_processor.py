from src.domain.chat_service import ChatService


class ChatProcessor:
    def __init__(self, chat_service: ChatService):
        self.chat_service = chat_service

    def send_message(self, character: str, message: str) -> str:
        return self.chat_service.send_message(character, message)
