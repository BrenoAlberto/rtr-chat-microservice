from abc import ABC, abstractmethod


class ChatService(ABC):
    @abstractmethod
    def send_message(self, character: str, message: str) -> str:
        pass
