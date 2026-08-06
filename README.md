# FoodOrder_Ai

## Project Description

FoodOrder_Ai is a lightweight multi-agent demo that demonstrates a retrieval-augmented generation (RAG) pipeline for a food-ordering assistant. The system composes small, focused agents (Customer, Recommendation, Restaurant, Order) that communicate via prompts and a mix of local data (menu.json) and LLM calls to produce menu recommendations and generate order summaries.


## Agent list

- CustomerAgent: parses user intent and extracts preferences.
- RecommendationAgent: reads `database/menu.json` and returns top recommendations.
- RestaurantAgent: simple accessor for the menu file.
- OrderAgent: formats a final order summary.

Open https://deva-0907-foodorder-ai-app-lh66qj.streamlit.app/ to view the running demo.

## Model-choice comparison

| Model | Provider | Cost | Latency | Strengths | Weaknesses | Recommended Use |
|---|---:|---:|---:|---|---|---|
| gpt-4o-mini | OpenRouter/OpenAI | Moderate | Low-Medium | Strong general reasoning, fast | Costly for high-volume | Customer intent parsing, natural summaries |
| openai/gpt-4o-mini | OpenAI via OpenRouter | Moderate | Low-Medium | Strong conversational abilities | Depends on provider latency | Primary conversational LLM |
| llama-3.1-8b-instant | Groq | Low | Low | Cost-effective, deterministic for retrieval use | Smaller context and fewer capabilities than larger models | Fast recommendation ranking in RAG |

Notes: choose models based on budget, latency, and required reasoning. For production, benchmark with representative prompts and traffic.

## Agent-communication diagram

<img width="1024" height="1536" alt="ChatGPT Image Aug 6, 2026, 10_48_30 AM" src="https://github.com/user-attachments/assets/c4e7d640-8892-41c2-a13f-ffb3acd22cf0" />


## Retrieval-Augmented Generation (RAG) pipeline

RAG combines an external knowledge source (here, `database/menu.json`) with a generative model. The typical flow in this repo is:

1. Query construction: the RecommendationAgent builds a prompt containing `customer_details` and an excerpt (or the whole) `menu.json`.
2. Retrieval step: the RestaurantAgent supplies the menu content (local retrieval).
3. Augmentation: the prompt includes retrieved facts so the LLM conditions on up-to-date, grounded information.
4. Generation: an LLM (Groq / OpenRouter) returns recommendations constrained by the supplied facts and rules.
.

## Live Streamlit demo link

- Local demo: https://deva-0907-foodorder-ai-app-lh66qj.streamlit.app/
## screenshot

<img width="942" height="470" alt="output" src="https://github.com/user-attachments/assets/7cf5d125-91ff-45ca-a030-aceac6dfcc24" />
<img width="928" height="808" alt="output1" src="https://github.com/user-attachments/assets/0a2abcc2-edef-4516-92d5-29f407a1b440" />
<img width="907" height="829" alt="output2" src="https://github.com/user-attachments/assets/945488e3-6231-42b2-91cf-2791687c4ca9" />
<img width="916" height="749" alt="output3" src="https://github.com/user-attachments/assets/ef9a25bb-e41a-45c7-922c-121bdb921199" />





## Next steps / Suggestions

- Replace local menu retrieval with a true retrieval layer (vectors + similarity search).
- Add tests and CI checks, and improve prompt templates with few-shot examples.
- Harden the `llm/openrouter.py` client wrapper to support fallback providers and retries.

# 👨‍💻 Author

T.Devanivethitha

IT Undergraduate

---
