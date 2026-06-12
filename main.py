from tool import get_weather
from recommendation_node import recommendation_node
from graph_builder import graph


location = input("Enter city and country (example: Delhi, India): ")
occasion = input(
    "Enter occasion "
    "(Office, Party, Wedding, Gym etc.): "
)

weather = get_weather(location)
result = graph.invoke(
    {
        "location": location,
        "occasion": occasion
    }
)
if "error" in result:

    print(result["error"])
else:

    print(
        f"\nLocation Found: "
        f"{result['weather_data']['city']}, "
        f"{result['weather_data']['country']}"
    )
    print(
        f"Occasion: "
        f"{result['occasion']}"
    )

    print("\nRecommended Outfit:\n")

    print(result["recommendation"])