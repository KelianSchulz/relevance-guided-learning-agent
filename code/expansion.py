

"""
expansion.py

Dieses Modul erweitert das bestehende (angepasste) Gedächtnis eines KI-Agenten,
indem es nach einem Zielwechsel neue, noch nicht gespeicherte relevante Texte aus der Artikelsammlung identifiziert
und dem Gedächtnis hinzufügt.

Input:
- agent_memory_adapted.json (aktuelles, angepasstes Wissen)
- articles.json (gesamte Textbasis)
- neues Ziel (als String)

Output:
- agent_memory_expanded.json (erweitertes Gedächtnis für neues Ziel)

Phase 4 des Projekts: Zielwandel + aktives Dazulernen.
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

