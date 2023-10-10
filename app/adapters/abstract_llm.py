from abc import ABC, abstractmethod
from fastapi import HTTPException

class AbstractLLM(ABC):
    @abstractmethod
    async def generate_text(self, prompt: str):
        pass

    @abstractmethod
    async def analyze_sentiment(self, text: str):
        pass

    @classmethod
    def get_adapter(cls, model: str):
        if model == "gpt-3-davinci":
            return GPT3Davinci()
        elif model == "claude-2":
            return Claude2()
        else:
            raise HTTPException(status_code=400, detail="Invalid model specified")

class GPT3Davinci(AbstractLLM):
    async def generate_text(self, prompt: str):
        # Implement the actual text generation with GPT-3 Davinci
        pass

    async def analyze_sentiment(self, text: str):
        # Implement sentiment analysis with GPT-3 Davinci
        pass

class Claude2(AbstractLLM):
    async def generate_text(self, prompt: str):
        # Implement the actual text generation with Claude-2
        pass

    async def analyze_sentiment(self, text: str):
        # Implement sentiment analysis with Claude-2
        pass
