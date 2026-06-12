from season_mapper import get_season

from rag.retriever import retrieve_fashion
from langgraph.graph import StateGraph
from typing import TypedDict
from tool import get_weather
from recommendation_node import recommendation_node

class WeatherState(TypedDict):

    location: str

    occasion: str

    weather_data: dict

    season: str

    retrieved_context: str

    recommendation: str

    error: str



def weather_node(state):

    
    weather = get_weather(
        state["location"]
    )

  
    if "error" in weather:

        state["error"] = weather["error"]

        return state

  
    state["weather_data"] = weather

    temp = weather["temperature"]

    state["season"] = get_season(temp)
    

    return state

def fashion_node(state):

    if "error" in state:

        return state

  
    recommendation = recommendation_node(

    state["weather_data"],

    state["occasion"],

    state["season"],

    state["retrieved_context"]
    )

    
    state["recommendation"] = recommendation

    return state


def retrieve_node(state):

    docs = retrieve_fashion(

        state["season"],

        state["occasion"]
    )

    context = "\n".join(

        [doc.page_content for doc in docs]
    )
    print("\n========== RETRIEVED PRODUCTS ==========\n")
    print(context)
    print("\n========================================\n")


    state["retrieved_context"] = context

    return state


builder = StateGraph(WeatherState)


builder.add_node(
    "weather",
    weather_node
)

builder.add_node(
    "retrieve",
    retrieve_node
)

builder.add_node(
    "fashion",
    fashion_node
)

builder.set_entry_point(
    "weather"
)

builder.add_edge(
    "weather",
    "retrieve"
)

builder.add_edge(
    "retrieve",
    "fashion"
)

graph = builder.compile()
