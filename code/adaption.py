import json
from embedding import embed_texts, embed_interest, compute_scores





# Filter relevant articles based on the new interest        
def filter_relevant_articles_adapted(articles, scores, threshold=0.5):
    adapted_memory = []
    for i in range(len(scores)):
        if scores[i] > threshold:
            article = articles[i].copy()
            article["score"] = float(scores[i])
            adapted_memory.append(article)
    return adapted_memory







# Save the adapted memory to a new JSON file
def save_memory_adapted(memory, path="data/agent_memory_adapted.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)            



