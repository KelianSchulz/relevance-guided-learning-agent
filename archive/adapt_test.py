from adaption import filter_relevant_articles_adapted, save_memory_adapted
from embedding import embed_texts, embed_interest, compute_scores
import json

# Altes Gedächtnis laden
with open("data/agent_memory.json", "r", encoding="utf-8") as f:
    memory = json.load(f)

# Neues Ziel
new_interest = "Reinforcement Learning"
new_interest_vec = embed_interest(new_interest)

# Texte vorbereiten
texts = [a["title"] + ". " + a["content"] for a in memory]
new_embeddings = embed_texts(texts)
new_scores = compute_scores(new_embeddings, new_interest_vec)

# Anpassung durchführen
adapted_memory = filter_relevant_articles_adapted(memory, new_scores, threshold=0.5)
save_memory_adapted(adapted_memory)
