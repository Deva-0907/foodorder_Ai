import json

from llm.groq import ask_groq


class RecommendationAgent:

    def recommend(self, customer_details, previous_recommendations=None):

        if previous_recommendations is None:
            previous_recommendations = []

        with open("database/menu.json", "r") as file:
            menu = json.load(file)

        prompt = f"""
You are a Food Recommendation Agent.

Customer Details:
{customer_details}

Restaurant Menu:
{menu}

Already Recommended Foods:
{previous_recommendations}

Rules:

1. Never recommend any food listed in "Already Recommended Foods".
2. Recommend the BEST THREE different foods.
3. Show:
   - Food Name
   - Price (LKR)
   - Reason

Return English only.
"""

        return ask_groq(prompt)