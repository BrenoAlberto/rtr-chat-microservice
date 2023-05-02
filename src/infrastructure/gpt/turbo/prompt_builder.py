from typing import List, Dict
from src.domain.prompt_builder import PromptBuilder


class GPTPromptBuilderTurbo(PromptBuilder):
    def build_prompt(
        self, character_description: str, message: str
    ) -> List[Dict[str, str]]:
        initial_message = {"role": "system", "content": character_description}
        return [
            initial_message,
            {"role": "user", "content": message},
        ]
