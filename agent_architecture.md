# 🧠 Self-Guided Learning Agent – Design Overview

---

## 1. Motivation
 
This project aims to explore a lightweight agent that can **select, retain, and adapt knowledge** intentionally –  
inspired by the idea of **goal-driven, relevance-based learning**.

---

## 2. Problem Statement

**Given:**  
- A set of unstructured textual data (e.g. Wikipedia articles)  
- A semantic goal or topic of interest (e.g. "Reinforcement Learning")

**Design an agent that can:**  
1. Identify which texts are most relevant to the goal  
2. Construct an internal memory of selected texts  
3. Adapt its memory when the goal changes  
4. Expand its knowledge if current memory is insufficient  
5. Explain its decisions in natural language

---

## 3. Architecture Overview

### 🔹 Input:
- `articles.json` (text + title)
- Semantic goal (string)

### 🔹 Core Modules:
| Module | Responsibility |
|--------|----------------|
| `embedding.py` | Embeds texts and goals into 384D semantic vectors  
| `memory.py` | Stores and filters knowledge based on cosine similarity  
| `adaptation.py` | Re-evaluates memory against a new goal  
| `expansion.py` | Searches and adds new relevant knowledge  
| `explanation.py` | Justifies why a text was selected  
| `visualize_memory.py` | Projects semantic memory space (t-SNE, Score bars)

---

## 4. Memory Evolution Process

```text
articles.json → [score] → agent_memory.json
                          ↓
                [filter vs. new goal]
                          ↓
             agent_memory_adapted.json
                          ↓
        [search for unseen relevant texts]
                          ↓
            agent_memory_expanded.json
                          ↓
         [explanation + visualization]


## 5. Example Output

```text
Explanation of memory selection: I chose the following texts because they have a cosine score >= 0.5:

🧠 Neural Networks  
→ Relevance: 0.576  
→ Good match with the goal.

🧠 Deep Learning  
→ Relevance: 0.541  
→ Good match with the goal.

🧠 Artificial Intelligence  
→ Relevance: 0.658  
→ Very strong semantic connection to the goal.
