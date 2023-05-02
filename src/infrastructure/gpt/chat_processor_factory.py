from .davinci.chat_service import DavinciChatService
from .turbo.chat_service import TurboChatService
# from .turbo.prompt_builder import GPTPromptBuilderTurbo
# from .davinci.prompt_builder import GPTPromptBuilderDavinci
from src.application.chat_processor import ChatProcessor

class ChatProcessorFactory:
    @staticmethod
    def create_chat_processor(api_key: str, model: str) -> ChatProcessor:
        if model == "gpt-3.5-turbo":
            # prompt_builder = GPTPromptBuilderTurbo()
            chat_service = TurboChatService(api_key)
        elif model == "davinci":
            # prompt_builder = GPTPromptBuilderDavinci()
            chat_service = DavinciChatService(api_key)

        return ChatProcessor(chat_service)
