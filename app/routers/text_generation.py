from fastapi import APIRouter, Depends
from ..adapters import AbstractLLM
from ..utils import Cache

router = APIRouter()
cache = Cache()

@router.post("/generate-text")
async def generate_text(prompt: str, model: str = "gpt-3-davinci"):
    adapter = AbstractLLM.get_adapter(model)
    cache_key = f"{model}-{prompt}"
    if cache.exists(cache_key):
        return cache.get(cache_key)
    text = await adapter.generate_text(prompt)
    cache.set(cache_key, text)
    return {"generated_text": text}