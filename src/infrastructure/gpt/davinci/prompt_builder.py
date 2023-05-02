from typing import List, Dict
from src.domain.prompt_builder import PromptBuilder


class GPTPromptBuilderDavinci(PromptBuilder):
    def build_prompt(
        self, character_description: str, message: str
    ) -> str:
        return f"Based on this description of the character: {character_description} , respond as the character: {message} "

