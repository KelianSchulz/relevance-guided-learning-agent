import re
from collections import Counter
from embedding import embed_texts, embed_interest, compute_scores, cosine_similarity
def extract_keywords(text, top_k=10):
   

    # 1. Nur Wörter (a-z), kleingeschrieben
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

    # 2. Häufigste Wörter zählen
    counter = Counter(words)

    # 3. Gib die häufigsten zurück
    keywords = []
    most_common = counter.most_common(top_k)

    for word, count in most_common:
        keywords.append(word)
    return keywords        

def rank_by_similarity(keywords, goal):
    # How much related is the goal vec to the text in cosine similarity
    word_embeddings = embed_texts(keywords)
    goal_vec = embed_interest(goal)
    
    scored_keywords = []

    for i, word in enumerate(keywords):
        score = cosine_similarity(word_embeddings[i], goal_vec)
        scored_keywords.append((word,score))

    scored_keywords.sort(key=lambda x: x[1], reverse=True)
    
    return scored_keywords    


def explain_keywords_for_text(text, goal, top_k=3):
    keywords = extract_keywords(text)
    scored = rank_by_similarity(keywords, goal)

    top_keywords = []
    for word, score in scored[:top_k]:
        top_keywords.append(word)

    explanation = (
    f"This text contains key terms such as "
    f"{', '.join(top_keywords)}, which are strongly related to the goal \"{goal}\"."
)
    return explanation         