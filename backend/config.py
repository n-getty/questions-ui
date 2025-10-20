import os
import json
BACKEND_READY = os.environ.get("QUESTIONSUI_BACKEND_READY", "true").lower() == "true" # Set to True when the LLM API is ready for requests.
SQLALCHEMY_DATABASE_URL = os.environ.get("QUESTIONSUI_SQLALCHEMY_DATABASE_URL", "sqlite:///db/questions.db")
LLM_API_BASE_URL = os.environ.get("QUESTIONSUI_AI_API", "https://data-portal-dev.cels.anl.gov/resource_server/sophia/vllm/v1/") # Replace it.
MODEL_NAME_MAP = json.loads(os.environ.get("QUESTIONSUI_MODEL_MAP", '{"Phi1.5": "microsoft/phi-1_5"}'))
EVENT_PASSWORD = os.environ.get("QUESTIONSUI_EVENT_PASSWORD", "anllabstyle")
SUGGESTION_MODEL_NAME = os.environ.get("QUESTIONSUI_SUGGESTION_MODEL_NAME", "gpt-3.5-turbo")
