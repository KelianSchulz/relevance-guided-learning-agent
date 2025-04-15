import json
from sentence_transformers import SentenceTransformer
import numpy as np

with open("data/articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# for article in articles:
#     print(article["title"])
#Load Model
model = SentenceTransformer('all-MiniLM-L6-v2')

#Comnbine Title with Content
texts = [a["title"] + ". " + a["content"] for a in articles]

embeddings = model.encode(texts)

target_interest = "Reinforcement Learning"
interest_vec = model.encode([target_interest])[0]


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = [cosine_similarity(e,interest_vec) for e in embeddings]

top_indices = np.argsort(scores)[-5:][::-1]
for i in top_indices:
    print(f"Score: {scores[i]:.3f} | Title: {articles[i]['title']}")
