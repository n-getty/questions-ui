import openai
from openai import AsyncOpenAI
from typing import Optional
from config import LLM_API_BASE_URL, SUGGESTION_MODEL_NAME
import schemas

async def get_suggestion_async(
    prompt: str,
    system_prompt: str,
    api_key: str,
) -> Optional[schemas.Suggestion]:
    """
    Return the suggestion for a given prompt in an asynchronous way.
    """
    try:
        client = AsyncOpenAI(base_url=LLM_API_BASE_URL, api_key=api_key)
        chat_completion = await client.chat.completions.create(
            model=SUGGESTION_MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        suggestion = chat_completion.choices[0].message.content
        if suggestion:
            return schemas.Suggestion(suggestion=suggestion)
        return None
    except openai.APITimeoutError:
        raise TimeoutError(f"{SUGGESTION_MODEL_NAME} timed out")
    except openai.BadRequestError:
        return None
