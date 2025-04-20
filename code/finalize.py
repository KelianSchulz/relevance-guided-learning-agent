import json



def merge_adapted_and_expanded(adapted_path, expanded_path, final_path="data/agent_memory_final.json"):
    with open(adapted_path, "r", encoding="utf-8") as f:
        adapted = json.load(f)
    with open(expanded_path, "r", encoding="utf-8") as f:
        expanded = json.load(f)

    # Duplikate anhand von Titeln entfernen
    seen_titles = set()
    final_memory = []

    for article in adapted + expanded:
        title = article["title"]
        if title not in seen_titles:
            final_memory.append(article)
            seen_titles.add(title)

    with open(final_path, "w", encoding="utf-8") as f:
        json.dump(final_memory, f, indent=4, ensure_ascii=False)
