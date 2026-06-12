from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def recommendation_node(

    weather_data,

    occasion,

    season,

    retrieved_context
):

    prompt = f"""
You are an expert women's fashion stylist.

Current Weather:

{weather_data}

Season:

{season}

Occasion:

{occasion}

Retrieved Fashion Products:

{retrieved_context}

Use the retrieved products as inspiration.

Recommend:

1. Topwear

2. Bottomwear

3. Footwear

4. Accessories

Explain why each recommendation
suits the weather and occasion.
"""

    response = llm.invoke(
        prompt
    )

    return response.content