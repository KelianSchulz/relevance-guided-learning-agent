import json

def filter_relevant_articles(articles, scores, threshold=0.5):
    memory = []
    for i in range(len(scores)):
        if scores[i] > threshold:
            article = articles[i].copy()
            article["score"] = float(scores[i])
            memory.append(article)
    return memory


def save_memory(memory, path="data/agent_memory.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)
