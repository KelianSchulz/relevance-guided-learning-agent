import json
from embedding import embed_texts, embed_interest, compute_scores
from memory import filter_relevant_articles, save_memory

def run_agent(data_path, interest, threshold=0.5):
    with open(data_path, "r", encoding="utf-8") as f:
        articles = json.load(f)

    texts = [a["title"] + ". " + a["content"] for a in articles]
    embeddings = embed_texts(texts)
    interest_vec = embed_interest(interest)
    scores = compute_scores(embeddings, interest_vec)

    top_indices = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)[:5]
    print("\n📊 Top 5 relevant texts:")
    for i in top_indices:
        print(f"Score: {scores[i]:.3f} | Title: {articles[i]['title']}")

    memory = filter_relevant_articles(articles, scores, threshold)
    save_memory(memory)
    print(f"Interest:{interest}")
    print(f"\n✅ Agent memory saved. {len(memory)} articles stored.\n")
