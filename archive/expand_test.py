from code.expansion import expanded_memory, save_memory


new_goal = "Reinforcement Learning"


expanded = expanded_memory(
    adapted_memory_path="data/agent_memory_adapted.json",
    articles_path="data/articles.json",
    new_goal=new_goal,
    output_path="data/agent_memory_expanded.json",
    threshold=0.5
)

# Speichern
save_memory(expanded, path="data/agent_memory_expanded.json")
