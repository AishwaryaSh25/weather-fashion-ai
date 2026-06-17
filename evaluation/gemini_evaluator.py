from deepeval.models import DeepEvalBaseLLM

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

import os

load_dotenv()


class GeminiEvaluator(DeepEvalBaseLLM):

    def __init__(self):

        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv(
                "GOOGLE_API_KEY"
            )
        )

    def load_model(self):

        return self.model

    def generate(self, prompt: str) -> str:

        response = self.model.invoke(
            prompt
        )

        return response.content

    async def a_generate(
        self,
        prompt: str
    ) -> str:

        response = await self.model.ainvoke(
            prompt
        )

        return response.content

    def get_model_name(self):

        return "Gemini-2.5-Flash"