from llm.openrouter import ask_openrouter


class CustomerAgent:

    def understand_customer(self, user_input):

        prompt = f"""
You are a Customer Understanding Agent.

Extract the following information from the user's request.

- Food preference
- Budget
- Cuisine
- Spice level
- Quantity

User Request:
{user_input}

Return the result in a simple readable format.
"""

        return ask_openrouter(prompt)