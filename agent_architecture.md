# 🧠 Self-Guided Learning Agent – Architecture & Design (v2)

---

## 1. Motivation

Many machine learning systems passively process data.  
This project explores a lightweight learning agent that **actively selects**, **retains**, and **justifies** what it learns, based on a **semantic goal**.  
The focus is on relevance-guided knowledge selection and **explainability** – laying groundwork for goal-driven, interpretable AI.

---

## 2. Problem Statement

**Given:**
- A corpus of unstructured texts (e.g. Wikipedia-style articles)
- A semantic target (e.g. "Reinforcement Learning")

**Build an agent that:**
1. Identifies relevant content
2. Constructs an internal memory
3. Adapts when goals change
4. Expands knowledge if needed
5. Explains why knowledge was selected

---

## 3. System Pipeline

```text
                ┌────────────┐
                │  Articles  │
                └─────┬──────┘
                      ↓
               ┌─────────────┐
               │ run_agent() │  ← Selection
               └─────┬───────┘
             memory.json
                      ↓
       ┌────────────────────────────┐
       │ filter_relevant_articles() │ ← Adaption
       └─────────────┬──────────────┘
             memory_adapted.json
                      ↓
        ┌──────────────────────────┐
        │ expand_memory_if_needed │ ← Expansion
        └─────────────┬───────────┘
             memory_expanded.json
                      ↓
    ┌─────────────────────────────────────┐
    │ merge_adapted_and_expanded()        │ ← Final knowledge state
    └─────────────────────────────────────┘
             memory_final.json
                      ↓
    ┌─────────────────────────────────────┐
    │ explain_memory()                    │ ← Explanation
    └─────────────────────────────────────┘
```

---

## 4. Core Modules

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

## 5. Example Output (v2)

```text
🧠 Deep learning  
→ Relevance: 0.541  
→ Good match with the goal.  
This text contains key terms such as learning, supervised, neural,  
which are strongly related to the goal "Reinforcement Learning".
```

---

## 6. Explainability: Score + Concept Level

- Cosine score: sentence-level embedding comparison
- Conceptual explanation: keyword extraction + semantic similarity
- Output: Natural language summary of **why** this text was selected

---

## 7. Limitations & Next Steps

| Limit | Opportunity |
|-------|-------------|
| No concept hierarchy | → Add knowledge graphs or ontologies  
| Goal must be provided manually | → Enable self-guided goal generation  
| No forgetting yet | → Implement memory decay or prioritization  
| Currently single-goal | → Extend to multi-goal agents with conflict resolution

---

## 8. Author & Vision

Built by Kelian Schulz  
As part of an independent research journey toward research-focused AI  
(e.g. future application at Bosch Center for Artificial Intelligence, BCAI)

Goal: Understand and design agents that not only learn – but explain, reflect, and grow.
