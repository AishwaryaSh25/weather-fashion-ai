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

    # Weather API returned an error
    if "error" in weather:

        state["error"] = weather["error"]

        return state

    # Store weather data
    state["weather_data"] = weather

    temp = weather.get("temperature")

    # Safety check
    if temp is None:

        state["error"] = (
            "Unable to determine weather for the given location."
        )

        return state

    state["season"] = get_season(temp)

    return state


def retrieve_node(state):

    # Stop if weather lookup failed
    if state.get("error"):

        return state

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


def fashion_node(state):

    # Stop if any previous node failed
    if state.get("error"):

        return state

    recommendation = recommendation_node(

        state["weather_data"],

        state["occasion"],

        state["season"],

        state["retrieved_context"]
    )

    state["recommendation"] = recommendation

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