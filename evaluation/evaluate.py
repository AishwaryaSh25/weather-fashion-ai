import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from graph_builder import graph

from deepeval.metrics import AnswerRelevancyMetric

from deepeval.test_case import LLMTestCase

from gemini_evaluator import GeminiEvaluator


judge_model = GeminiEvaluator()


metric = AnswerRelevancyMetric(
    threshold=0.7,
    model=judge_model
)


test_cases = [

    {
        "location": "Delhi, India",
        "occasion": "Office"
    },

    {
        "location": "Mumbai, India",
        "occasion": "Party"
    },

    {
        "location": "London, UK",
        "occasion": "Casual"
    }

]


scores = []


for test in test_cases:

    print("\n======================")

    print(
        f"Testing: "
        f"{test['location']} | "
        f"{test['occasion']}"
    )

    result = graph.invoke(
        {
            "location": test["location"],
            "occasion": test["occasion"]
        }
    )

    recommendation = result[
        "recommendation"
    ]

    test_case = LLMTestCase(

        input=f"""
Location:
{test['location']}

Occasion:
{test['occasion']}
""",

        actual_output=recommendation
    )

    metric.measure(
        test_case
    )

    score = metric.score

    scores.append(
        score
    )

    print(
        f"Score: {score:.2f}"
    )


average_score = (
    sum(scores)
    /
    len(scores)
)

print("\n======================")

print(
    f"Average Relevancy Score: "
    f"{average_score:.2f}"
)

print("======================")