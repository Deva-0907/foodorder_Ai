from llm.openrouter import ask_openrouter


class CustomerAgent:

    def understand_customer(self, user_input):

      prompt = f"""
You are a Customer Agent.

The customer said:
_
{user_input}

Your job is:

1. Understand the request.
2. Extract:
- Food Preference
- Budget
- Cuisine
- Quantity
3. Suggest FIVE possible foods the customer may like.

Return the result in this format.

Food Preference:
Budget:
Cuisine:
Quantity:

Suggested Foods:
1.
2.
3.
4.
5.

Use English only.
"""

      return ask_openrouter(prompt)