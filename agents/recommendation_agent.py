import json

from llm.groq import ask_groq


class RecommendationAgent:

    def recommend(self, customer_details):

        with open("database/menu.json", "r") as file:
            menu = json.load(file)

        prompt = f"""
You are a Food Recommendation Agent.

Customer Details

{customer_details}

Restaurant Menu

{menu}

Recommend THREE foods.

For each food include:

Food Name

Price (LKR)

Reason

Return only English.
"""

        return ask_groq(prompt)