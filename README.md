# 🧠 Relevance-Guided Learning Agent

A modular AI system that **decides what it wants to learn**,  
based on semantic relevance to a given goal.  
It selects, adapts, expands, and **explains** its own memory –  
not just by scores, but by meaning.

---

## 🌱 Motivation

Most models passively consume training data.  
This one asks:

> “What should I learn – and why?”

Inspired by:
- Curriculum learning
- Cognitive memory systems
- Attention-based selection
- Explainable AI & concept-based reasoning

---

## 🔍 What It Does

- 🧠 **Semantic Selection**: Chooses relevant documents from a pool  
- 🔁 **Goal Adaptation**: Filters memory if the learning goal changes  
- ➕ **Knowledge Expansion**: Adds new, previously unseen texts if memory is too weak  
- 💬 **Explanation Layer**: For each memory item:
  - Cosine similarity score to the goal
  - Qualitative explanation of relevance
  - Keyword-level semantic justification

---

## ✨ Example Output

```text
🧠 Neural Networks  
→ Relevance: 0.577  
→ Good match with the goal.  
→ This text contains key terms such as neural, networks, neuron, which are strongly related to the goal "Reinforcement Learning".
```

---

## 📁 Project Structure

```
.
├── code/                          # Core logic (agent, memory, explanation, etc.)
│   ├── main.py
│   ├── embedding.py
│   ├── adaptation.py
│   ├── expansion.py
│   ├── explanation.py
│   ├── explain_keywords.py
│   ├── finalize.py
│   └── visualize_memory.py
│
├── data/                          # Input and memory data
│   ├── articles.json
│   ├── agent_memory.json
│   ├── agent_memory_adapted.json
│   ├── agent_memory_expanded.json
│   └── agent_memory_final.json
│
├── agent_design.md                # Research-oriented documentation
├── requirements.txt
└── README.md                      # You are here
```

---

## 🚀 Quickstart

```bash
pip install -r requirements.txt
python main.py
```

To visualize what the agent retained:

```bash
python visualize_memory.py
```

---

## 🧪 Version History

- **v1.0** – Core agent: selection, adaptation, expansion, visualization  
- **v2.0** – Added explanation layer with semantic keyword-based justification  

---

## ✍️ Author

Built by **Kelian Schulz**  
Project goal: Build research-ready, interpretable agent architectures  
with a long-term view on memory-guided learning and symbolic AI integration.
