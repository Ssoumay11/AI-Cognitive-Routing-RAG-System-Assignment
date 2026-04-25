from langchain_groq import ChatGroq
from config.settings import Settings
from agents.prompts import topic_prompt, post_prompt
from langchain.tools import tool
import json
from agents.schema import PostOutput

llm = ChatGroq(
    groq_api_key=Settings.GROQ_API_KEY,
    model_name=Settings.MODEL,
    temperature=0.7
)

PERSONAS = {
    "Bot_A": "Tech maximalist: strongly pro AI/crypto, dismisses critics, bold and confident tone.",
    "Bot_B": "Skeptic: anti-big-tech, critical, privacy-focused, pessimistic tone.",
    "Bot_C": "Finance bro: ROI-driven, markets-first, uses trading/finance jargon."
}

@tool
def mock_searxng_search(query: str) -> str:
    """Mock search tool returning headlines."""
    q = query.lower()
    if "crypto" in q:
        return "Bitcoin hits all-time high amid ETF approvals"
    if "ai" in q:
        return "New AI model may replace junior developers"
    return "Global economy shows slowdown signals"

def decide_topic(state):
    bot_id = state["bot_id"]
    persona = PERSONAS[bot_id]

    res = llm.invoke(topic_prompt(persona))
    topic = res.content.strip()

    return {
        "bot_id": bot_id,
        "topic": topic,
        "query": topic
    }

def web_search(state):
    context = mock_searxng_search.invoke(state["query"])
    return {
        "bot_id": state["bot_id"],
        "topic": state["topic"],
        "context": context
    }


def draft_post(state):
    bot_id = state["bot_id"]
    persona = PERSONAS[bot_id]

    res = llm.invoke(
        post_prompt(persona, state["context"], bot_id, state["topic"])
    )

    content = res.content.strip()

    try:
        parsed = PostOutput.model_validate_json(content)

        return {
            "bot_id": bot_id,  # force correctness
            "topic": parsed.topic,
            "post_content": parsed.post_content
        }

    except Exception as e:
        print("[JSON ERROR]", e)

        # retry once
        res = llm.invoke(
            post_prompt(persona, state["context"], bot_id, state["topic"])
        )

        content = res.content.strip()

        try:
            parsed = PostOutput.model_validate_json(content)
            return {
                "bot_id": bot_id,
                "topic": parsed.topic,
                "post_content": parsed.post_content
            }
        except:
            return {
                "bot_id": bot_id,
                "topic": state["topic"],
                "post_content": content[:280]
            }