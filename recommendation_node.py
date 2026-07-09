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

Available Fashion Products:
{retrieved_context}

Use only the retrieved products as inspiration for your recommendations.

### Task
Recommend one item for each category:

- Topwear
- Bottomwear
- Footwear
- Accessories

### Guidelines
- Keep each explanation to **1-2 short sentences**.
- Mention why it suits the **weather** and **occasion**.
- Do not write long paragraphs.
- Use clear, concise, and easy-to-read language.
- If multiple suitable options exist, choose the best one.

### Output Format

Topwear:
- <Recommendation>
- Why: <Short reason>

Bottomwear:
- <Recommendation>
- Why: <Short reason>

Footwear:
- <Recommendation>
- Why: <Short reason>

Accessories:
- <Recommendation>
- Why: <Short reason>
"""

    response = llm.invoke(
        prompt
    )

    return response.content