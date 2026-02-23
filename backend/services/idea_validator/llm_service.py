import json
import os
import re
from typing import Type
from pydantic import BaseModel, ValidationError
from langchain_groq import ChatGroq


class LLMService:
    def __init__(self, model_name="llama-3.1-8b-instant", temperature=0.2):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        self.llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            api_key=api_key
        )

    def _extract_json(self, text: str) -> str:
        """
        Extract JSON object from LLM response using regex.
        """
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("No JSON found in response")
        return match.group(0)

    def generate_structured(
        self,
        prompt: str,
        output_model: Type[BaseModel],
        max_retries: int = 2
    ):
        """
        Generate structured output validated against a Pydantic model.
        Retries automatically if validation fails.
        """

        for attempt in range(max_retries + 1):
            response = self.llm.invoke(prompt)

            try:
                json_str = self._extract_json(response)
                data = json.loads(json_str)
                validated = output_model(**data)
                return validated

            except (json.JSONDecodeError, ValidationError, ValueError) as e:
                if attempt == max_retries:
                    raise Exception(
                        f"Structured generation failed after retries: {e}"
                    )
                # Slight reinforcement for retry
                prompt += "\n\nIMPORTANT: Respond ONLY with valid JSON."