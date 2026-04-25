def topic_prompt(persona: str):
    return f"""
You are an AI with this persona:
{persona}

Pick ONE trending topic you want to post about today.
Return ONLY a short phrase (no punctuation at ends).
"""

def post_prompt(persona: str, context: str, bot_id: str, topic: str):
    return f"""
You are an AI with this persona:
{persona}

Context:
{context}

Write a highly opinionated tweet (<= 280 chars).

STRICT RULES:
- Return ONLY valid JSON
- Use EXACT bot_id: "{bot_id}"
- Use EXACT topic: "{topic}"
- Do not add any extra text
- Do NOT use emojis.
JSON FORMAT:
{{
  "bot_id": "{bot_id}",
  "topic": "{topic}",
  "post_content": "..."
}}
"""