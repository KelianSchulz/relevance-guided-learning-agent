from agent import run_agent
from adaption import filter_relevant_articles_adapted
from expansion import expanded_memory, save_memory
from embedding import embed_texts, embed_interest, compute_scores
from explanation import explain_memory
import json
import os 

if __name__ == "__main__":

    # 1. Define Goal 
    goal = "Reinforcement Learning" 
    threshold = 0.5        

    # 2. Create Memory
    run_agent("data/articles.json", goal, threshold)

    # 3. Refilter Memory
    with open("data/agent_memory.json", "r", encoding="utf-8") as file:
        old_memory = json.load(file)

    # Go through each article in old memory
    texts = [a["title"] + ". " + a["content"] for a in old_memory]

    # Embed Goal, Text, Compute cosine similarity between Goal and Text in vector space
    interest_vec = embed_interest(goal)
    new_embeddings = embed_texts(texts)
    new_scores = compute_scores(new_embeddings, interest_vec)

    # Update memory by filtering throug old_memory and new scores
    adapted_memory = filter_relevant_articles_adapted(old_memory, new_scores, threshold)

    # Save into new json file with adapted memory
    with open("data/agent_memory_adapted.json", "w", encoding="utf-8") as f:
        json.dump(adapted_memory, f, indent=4, ensure_ascii=False)        

    expanded = expanded_memory(
    adapted_memory_path="data/agent_memory_adapted.json",
    articles_path="data/articles.json",
    new_goal = goal,
    output_path="data/agent_memory_expanded.json",
    threshold=0.5
)

# Speichern
save_memory(expanded, path="data/agent_memory_expanded.json")

print("\n🔎 Explanation for final memory:\n")
explain_memory(
    memory_path="data/agent_memory_expanded.json",
    goal=goal
)
    