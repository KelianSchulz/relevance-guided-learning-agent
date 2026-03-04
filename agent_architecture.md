# 🧠 Self-Guided Learning Agent – Architecture & Design (v2)



## 1. Core Modules

| Module                | Role                                                                 |
|-----------------------|----------------------------------------------------------------------|
| `embedding.py`        | Embeds texts and goals in semantic space (384D Sentence-BERT)       |
| `agent.py`            | Initial selection of relevant articles                               |
| `adaptation.py`       | Filters memory based on new goal                                     |
| `expansion.py`        | Finds new unseen texts that are relevant to the goal                 |
| `finalize.py`         | Merges adapted and expanded memory into a clean final representation |
| `explanation.py`      | Score-based and keyword-based natural language justification         |
| `explain_keywords.py` | Identifies semantically meaningful terms for each text               |
| `visualize_memory.py` | t-SNE and bar plots for memory visualization                         |

---

## 2. Example Output (v2)

```text
🧠 Deep learning  
→ Relevance: 0.541  
→ Good match with the goal.  
This text contains key terms such as learning, supervised, neural,  
which are strongly related to the goal "Reinforcement Learning".
```

---

## 3. Explainability: Score + Concept Level

- Cosine score: sentence-level embedding comparison
- Conceptual explanation: keyword extraction + semantic similarity
- Output: Natural language summary of **why** this text was selected

---

## 4. Limitations & Next Steps

| Limit | Opportunity |
|-------|-------------|
| No concept hierarchy | → Add knowledge graphs or ontologies  
| Goal must be provided manually | → Enable self-guided goal generation  
| No forgetting yet | → Implement memory decay or prioritization  
| Currently single-goal | → Extend to multi-goal agents with conflict resolution

---

## 8. Author 

Built by Kelian Schulz  


Goal: Understand and design agents that not only learn – but explain, reflect, and grow.
