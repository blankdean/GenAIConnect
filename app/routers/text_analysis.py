from fastapi import APIRouter
from ..adapters import AbstractLLM

router = APIRouter()

@router.post("/sentiment-analysis")
async def sentiment_analysis(text: str, model: str = "gpt-3-davinci"):
    adapter = AbstractLLM.get_adapter(model)
    sentiment = await adapter.sentiment_analysis(text)
    return {"sentiment": sentiment}

@router.post("/summarize-text")
async def summarize_text(text: str, model: str = "gpt-3-davinci"):
    adapter = AbstractLLM.get_adapter(model)
    summary = await adapter.summarize_text(text)
    return {"summary": summary}