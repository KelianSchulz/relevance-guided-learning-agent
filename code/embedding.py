from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    return model.encode(texts) # Vectorize texts

def embed_interest(interest_text):
    return model.encode([interest_text])[0] # Vectorize Goal for ex. "Machine Learning"

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)) # Calculate Cosine similarity

def compute_scores(embeddings, interest_vec):
    return [cosine_similarity(e, interest_vec) for e in embeddings] #Calculate Score 