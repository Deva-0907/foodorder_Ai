from llm.openrouter import ask_openrouter


class OrderAgent:

    def create_order(self, recommendation):

        prompt = f"""


{recommendation}

Include:

- Ordered Item
- Estimated Price
- Quantity

- Thank You Message


        return ask_openrouter(prompt)