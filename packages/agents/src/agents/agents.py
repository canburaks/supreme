from typing import Any, Callable, Literal, Union

from configs import AgentsSettings
from pydantic_ai import Agent
from pydantic_ai.models import Model
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.models.openai import OpenAIModel

PROVIDERS = Literal["openai", "anthropic", "gemini", "ollama", "openrouter", "deekseek"]
GEMINI_MODEL_NAMES = Literal[
    "gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp"
]
PROVIDER_MODEL_OUTPUT_TYPE = Callable[[str], Model]
settings = AgentsSettings()


def get_model_provider(
    provider_name: Union[str, PROVIDERS],
) -> PROVIDER_MODEL_OUTPUT_TYPE:
    if provider_name == "openai":

        def return_openai_model(model_name: str) -> Model:
            return OpenAIModel(
                api_key=settings.OPENAI_API_KEY,
                model_name=model_name,
            )

        return return_openai_model
    elif provider_name == "anthropic":

        def return_anthropic_model(model_name: str) -> Model:
            return OpenAIModel(
                api_key=settings.ANTHROPIC_API_KEY,
                model_name=model_name,
            )

        return return_anthropic_model
    elif provider_name == "ollama":

        def return_ollama_model(model_name: str) -> Model:
            return OllamaModel(
                base_url=settings.OLLAMA_URL,
                model_name=model_name,
            )

        return return_ollama_model
    elif provider_name == "openrouter":

        def return_openrouter_model(model_name: str) -> Model:
            return OpenAIModel(
                api_key=settings.OPENROUTER_API_KEY,
                base_url="https://openrouter.ai/api/v1",
                model_name=model_name,
            )

        return return_openrouter_model
    elif provider_name == "deekseek":

        def return_deekseek_model(model_name: str) -> Model:
            return OpenAIModel(
                model_name=model_name,
                api_key=settings.DEEPSEEK_API_KEY,
                base_url="https://api.deepseek.com",
            )

        return return_deekseek_model
    else:
        raise ValueError(f"Invalid model provider: {provider_name}")


def get_agent(kwargs: dict[str, Any]) -> Agent:
    provider_model_name: str = kwargs.pop("provider", "")
    if not provider_model_name:
        raise ValueError("provider is required")
    model_name = kwargs.pop("model", "")
    if not model_name:
        raise ValueError("model_name is required")

    provider_model: PROVIDER_MODEL_OUTPUT_TYPE = get_model_provider(
        provider_name=provider_model_name
    )
    model: Model = provider_model(model_name)

    return Agent(model, **kwargs)
