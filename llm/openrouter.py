import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def ask_openrouter(prompt):

    response = client.chat.completions.create(
 feature/agents
        model="gpt-4o-mini",

        feature/llm
        model="openai/gpt-4o-mini",

        model="gpt-4o-mini",
        main
main
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content