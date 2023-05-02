from abc import ABC, abstractmethod
from typing import List, Dict


class PromptBuilder(ABC):
    @abstractmethod
    def build_prompt(
        self, character_description: str, message: str
    ) -> List[Dict[str, str]]:
        pass
