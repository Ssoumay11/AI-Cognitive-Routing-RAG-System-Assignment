def build_context(parent, history, reply):
    context = f"[Parent - Human]: {parent}\n\n"

    for i, h in enumerate(history):
        context += f"[Comment {i+1}]: {h}\n"

    context += f"\n[Latest Human]: {reply}\n"

    return context