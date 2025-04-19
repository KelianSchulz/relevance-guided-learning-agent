"""
explanation.py

Dieses Modul erzeugt einfache, nachvollziehbare Begründungen für die
Auswahl gespeicherter Texte im Agentengedächtnis – auf Basis ihrer
semantischen Ähnlichkeit zum Ziel.

Ziel: interpretierbares Verhalten & Transparenz.
"""
from embedding import embed_interest, compute_scores, embed_texts, cosine_similarity


import json
def explain_memory(memory_path, goal):
    with open (memory_path, "r", encoding="utf-8") as f:
        memory = json.load(f)

    goal_vec = embed_interest(goal)
    texts = [a["title"] + ". " + a["content"] for a in memory]
    titles = [a["title"] for a in memory]
    embeddings = embed_texts(texts)
    scores = compute_scores(embeddings, goal_vec)

    print(f"Erklärung der Gedächtniswahl: Ich habe folgende Texte ausgewählt, weil sie einen Cosine score >= 0.5 haben:")
    for i in range(len(memory)):
        print(type(embeddings[i]), type(goal_vec))
        score = cosine_similarity(embeddings[i], goal_vec)
        print(f"🧠 {titles[i]}")
        print(f"→ Relevanz: {scores[i]:.3f}")
        if score > 0.7:
            print("→ Sehr starke semantische Verbindung zum Ziel.\n")
        elif score > 0.5:
            print("→ Gute Übereinstimmung mit dem Ziel.\n")
        elif score > 0.3:
            print("→ Leichte thematische Nähe, aber nicht dominant.\n")
        else:
            print("→ Kaum relevante Verbindung. (Warum wurde das gespeichert? Höaääöä)\n")




            #Notiz:
            #Warum ist der Score anders als in der expansion????!?!?!!?!?!?!!?!?!?!?!!?!?!?!?!?!