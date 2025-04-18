# Automization to fill Articles in json file. 

import wikipedia
import json
import os


topics = [
    "Artificial intelligence",
    "Reinforcement learning",
    "Neural networks",
    "Machine learning",
    "Deep learning",
    "Convolutional neural networks",
    "Overfitting",
    "Backpropagation",
    "Gradient descent",
    "Bayesian networks",
    "Regularization (machine learning)",
    "Markov decision process",
    "Self-supervised learning"
]

#Output path
output_path = os.path.join("data", "articles.json")

articles = []

for topic in topics:
    try:
        page = wikipedia.page(topic)
        summary = wikipedia.summary(topic, sentences=5)  # Nur die ersten paar Sätze
        articles.append({
            "title": topic,
            "content": summary
        })
        print(f"✅ Loaded: {topic}")
    except Exception as e:
        print(f"⚠️ Failed to load '{topic}': {e}")

# Save as JSON
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)

print(f"\n✅ Saved {len(articles)} articles to '{output_path}'")
