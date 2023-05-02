import openai
from src.domain.chat_service import ChatService
from .prompt_builder import GPTPromptBuilderTurbo 


class TurboChatService(ChatService):
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.prompt_builder = GPTPromptBuilderTurbo()

    def send_message(
        self, character_description: str, message: str
    ) -> str:
        prompt = self.prompt_builder.build_prompt(character_description, message)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
        )
        return response.choices[0]['message']['content'].strip()
