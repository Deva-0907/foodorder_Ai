import json

from llm.groq import ask_groq


class RecommendationAgent:

    def recommend(self, customer_details):

        with open("database/menu.json", "r") as file:
            menu = json.load(file)

        prompt = f"""
You are a Food Recommendation Agent.

Customer Details:

{customer_details}

Available Menu:

{menu}

Recommend the best food.

Explain why.
"""

        return ask_groq(prompt)