

"""
expansion.py

This module expands the existing (adapted) memory of an AI agent
by identifying and adding new, relevant texts from the article collection
that have not yet been stored, after a change in the agent's goal.

Input:
- agent_memory_adapted.json (current, adapted knowledge)
- articles.json (complete text base)
- new goal (as a string)

Output:
- agent_memory_expanded.json (expanded memory for the new goal)

Phase 4 of the project: Goal shift + active learning.
"""


import json
from embedding import embed_interest, embed_texts, compute_scores, cosine_similarity


def expanded_memory(adapted_memory_path, articles_path, new_goal, output_path, threshold=0.5):
    goal_vec = embed_interest(new_goal)
    expansion_list = []
    #Load adapted memory
    with open(adapted_memory_path, 'r', encoding='utf-8') as file:
        adapted_memory = json.load(file)
    
    #Load all articles
    with open(articles_path, 'r', encoding="utf-8") as file:
        all_articles = json.load(file)        

    # Known articles
    known_titles = set(a["title"] for a in adapted_memory)        

    # Unknown articles
    unseen_articles = [a for a in all_articles if a["title"] not in known_titles]

    new_embedded_articles = embed_texts(unseen_articles)
    new_scores = compute_scores(new_embedded_articles, goal_vec)

    for i in range(len(unseen_articles)):
        if new_scores[i] > threshold:
            article = unseen_articles[i].copy()
            article["score"] = float(new_scores[i])
            expansion_list.append(article)

    return expansion_list        
        

def save_memory(memory, path="data/agent_memory_expanded.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)        

