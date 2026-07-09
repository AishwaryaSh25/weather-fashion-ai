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

### Context
Weather:
{weather_data}

Season:
{season}

Occasion:
{occasion}

Retrieved Fashion Products:
{retrieved_context}

### Instructions
- Use the retrieved products as your primary source of recommendations.
- Recommend exactly one item for each category:
  1. Topwear
  2. Bottomwear
  3. Footwear
  4. Accessories
- If a suitable retrieved product is unavailable for a category, recommend a common women's fashion item that complements the retrieved products and clearly mention that it is a general suggestion.
- Prioritize comfort, style, and suitability for the given weather, season, and occasion.
- Keep each explanation to one short sentence.
- Do not write long paragraphs.
- Do not repeat the weather or occasion in every explanation.

### Output Format

Topwear
- Recommendation: <Product Name>
- Source: Retrieved Product / General Suggestion
- Why: <One short sentence>

Bottomwear
- Recommendation: <Product Name>
- Source: Retrieved Product / General Suggestion
- Why: <One short sentence>

Footwear
- Recommendation: <Product Name>
- Source: Retrieved Product / General Suggestion
- Why: <One short sentence>

Accessories
- Recommendation: <Product Name>
- Source: Retrieved Product / General Suggestion
- Why: <One short sentence>
"""

    response = llm.invoke(
        prompt
    )

    return response.content