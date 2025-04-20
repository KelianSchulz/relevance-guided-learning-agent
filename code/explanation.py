"""
explanation.py

This module generates simple, understandable explanations for the
selection of stored texts in the agent’s memory – based on their
semantic similarity to the goal.

Objective: interpretable behavior & transparency.
"""
from embedding import embed_interest, compute_scores, embed_texts, cosine_similarity
from explain_keywords import explain_keywords_for_text

import json
def explain_memory(memory_path, goal):
    with open(memory_path, "r", encoding="utf-8") as f:
        memory = json.load(f)

    goal_vec = embed_interest(goal)
    texts = [a["title"] + ". " + a["content"] for a in memory]
    titles = [a["title"] for a in memory]
    
    

    print(f"Explanation of memory selection: I chose the following texts because they have a cosine score >= 0.5:")
    for i in range(len(memory)):
        
        score = memory[i]["score"]
        print(f"🧠 {titles[i]}")
        print(f"→ Relevance: {score:.3f}")
        if score > 0.7:
            print("→ Very strong semantic connection to the goal.\n")
        elif score > 0.5:
            print("→ Good match with the goal.\n")
        elif score > 0.3:
            print("→ Slight thematic proximity, but not dominant.\n")
        else:
            print("→ Hardly any relevant connection. (Why was this stored?)\n")
        keyword_explanation = explain_keywords_for_text(
            memory[i]["title"] + ". " + memory[i]["content"], goal
            )

        print(keyword_explanation)
        print()  