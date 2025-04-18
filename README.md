# relevance-guided-learning-agent

This project explores the idea of a minimal AI system that **selects what it wants to learn** from a set of documents – based on a *defined interest*.

It chooses, scores, filters and adapts what it stores – with the long-term goal of exploring:
- Relevance-driven learning
- Memory modulation
- Self-curated knowledge graphs

Inspired by ideas in curriculum learning, attention-based selection, and the emerging concept of curiosity-driven AI.

## 🌱 Core Idea

Most machine learning models consume what we give them.  
This one *asks*:

> “What should I learn – and why?”

## 🚀 Goals

- Implement a lightweight system that can:
  - evaluate textual inputs
  - select relevant samples
  - refine its "knowledge set"
- Start with scoring strategies (e.g. cosine similarity to a goal-topic embedding)
- Later: introduce forgetting, self-adaptation, and learning path planning

## 🧠 Technologies

- Python
- SentenceTransformers / BERT / TF-IDF
- Pandas, Matplotlib
- (optionally) PyTorch or small transformer models

## 📁 Structure

- `src/`: Core logic
- `data/`: Small curated dataset of texts (e.g. Wikipedia, abstracts, blogposts)
- `notebooks/`: Visual experiments
- `experiments/`: Different agent runs, logging
- `README.md`: You are here.

## 🔭 Next step

Start building a minimal baseline agent that can:
- read 100 texts
- decide which 10 are most relevant to a target
- justify its choice

Let’s build something that learns with direction.
