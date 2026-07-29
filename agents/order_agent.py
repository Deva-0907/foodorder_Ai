from llm.openrouter import ask_openrouter


class OrderAgent:

    def create_order(self, recommendation):

        prompt = f"""
Create a professional food order summary.

Recommendation:

{recommendation}

Include:

- Ordered Item
- Estimated Price
- Quantity

"""

        return ask_openrouter(prompt)