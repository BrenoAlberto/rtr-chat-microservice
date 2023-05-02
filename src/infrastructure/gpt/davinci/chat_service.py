import openai
from src.domain.chat_service import ChatService
from .prompt_builder import GPTPromptBuilderDavinci

class DavinciChatService(ChatService):
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.prompt_builder = GPTPromptBuilderDavinci()

    def send_message(self, character: str, message: str) -> str:
        prompt = self.prompt_builder.build_prompt(character, message)
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=600,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
