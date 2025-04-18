import numpy as np
import matplotlib.pyplot as plt

# Wir simulieren 2D-Vektoren für 6 "Texte"
# Gruppe 1: Bedeutet "KI"
# Gruppe 2: Bedeutet "Essen"

# KI-nahe Texte
texts_ki = {
    "Reinforcement Learning": np.array([1.0, 2.0]),
    "Policy Gradient": np.array([1.5, 2.2]),
    "Neural Network": np.array([0.8, 1.8]),
}

# Essensnahe Texte
texts_essen = {
    "Lasagne Rezept": np.array([-2.0, 0.5]),
    "Spaghetti Bolognese": np.array([-2.2, 0.8]),
    "Pasta kochen": np.array([-1.8, 0.3]),
}

# Visualisieren
plt.figure(figsize=(8, 6))

# KI-Punkte
for label, vec in texts_ki.items():
    plt.scatter(vec[0], vec[1], color='blue')
    plt.text(vec[0]+0.1, vec[1], label, fontsize=10, color='blue')

# Essens-Punkte
for label, vec in texts_essen.items():
    plt.scatter(vec[0], vec[1], color='green')
    plt.text(vec[0]+0.1, vec[1], label, fontsize=10, color='green')

plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.title("Vereinfachter 2D-Vektorraum: KI vs. Essen")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.tight_layout()
plt.show()
