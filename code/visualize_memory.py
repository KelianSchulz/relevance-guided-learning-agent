"""
visualize_memory.py

Dieses Modul zeigt das aktuelle Gedächtnis des Agenten visuell:
- Relevanz der Texte (Score)
- Nähe der Bedeutungen im semantischen Raum (t-SNE)

Input: data/agent_memory_expanded.json
"""


import json
import matplotlib.pyplot as plt

# 1. Load final Memory
with open("data/agent_memory_expanded.json", "r", encoding="utf-8") as f:
    memory = json.load(f)

# 2. Sort scores descending
# (Hier wird angenommen, dass jeder Eintrag in memory ein Dictionary mit "title" und "score" ist)
# Beispiel: memory = [{"title": "Text 1", "score": 0.8}, {"title": "Text 2", "score": 0.6}, ...]
memory.sort(key=lambda x: x["score"], reverse=True)

# 3. extract titles and scores for plotting

titles = [entry["title"] for entry in memory]
scores = [entry["score"] for entry in memory]

# 4. Plot the scores
plt.figure(figsize=(10, 6))
bars = plt.barh(titles, scores, color='skyblue')
plt.xlabel("Relevanz (Cosine Score)")
plt.title("Gespeicherte Texte nach Relevanz zum Ziel")
plt.gca().invert_yaxis()
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

from sklearn.manifold import TSNE
from embedding import embed_texts
# 1. Lade alle Artikel
with open("data/articles.json", "r", encoding="utf-8") as f:
    all_articles = json.load(f)

# 2. Extrahiere Titel des gelernten Gedächtnisses
kept_titles = set([entry["title"] for entry in memory])

# 3. Trenne in behaltene und ignorierte Texte
texts_kept = [a["title"] + ". " + a["content"] for a in all_articles if a["title"] in kept_titles]
texts_unseen = [a["title"] + ". " + a["content"] for a in all_articles if a["title"] not in kept_titles]
titles_kept = [a["title"] for a in all_articles if a["title"] in kept_titles]
titles_unseen = [a["title"] for a in all_articles if a["title"] not in kept_titles]

# 4. Combine und embedde
texts_combined = texts_kept + texts_unseen
titles_combined = titles_kept + titles_unseen
labels = ['Gelernt'] * len(texts_kept) + ['Ignoriert'] * len(texts_unseen)

embeddings = embed_texts(texts_combined)

# 5. t-SNE-Projektion
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

tsne = TSNE(n_components=2, perplexity=min(5, len(texts_combined)-1), random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

# 6. Visualisierung mit Farben
plt.figure(figsize=(10, 8))
for i, (x, y) in enumerate(embeddings_2d):
    color = 'blue' if labels[i] == 'Gelernt' else 'red'
    plt.scatter(x, y, color=color, label=labels[i] if i == 0 or labels[i] != labels[i - 1] else "")
    plt.text(x + 0.3, y, titles_combined[i], fontsize=8)

plt.title("t-SNE: Vergleich gespeicherte vs. ignorierte Texte")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
