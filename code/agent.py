import json
from embedding import embed_texts, embed_interest, compute_scores
from memory import filter_relevant_articles, save_memory


def run_agent(data_path, interest, threshold = 0.5):
    #Load Texts
    with open(data_path,"r", encoding="utf-8") as f:
        articles = json.load(f)
    texts = [a["title"] + ". " + a["content"] for a in articles]
