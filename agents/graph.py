from langgraph.graph import StateGraph
from agents.nodes import decide_topic, web_search, draft_post

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("decide", decide_topic)
    graph.add_node("search", web_search)
    graph.add_node("draft", draft_post)

    graph.set_entry_point("decide")
    graph.add_edge("decide", "search")
    graph.add_edge("search", "draft")

    return graph.compile()