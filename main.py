# This entrypoint file to be used in development. Start by reading README.md
import sea_level_predictor
from unittest import main

# Vérifier quelle fonction est définie dans sea_level_predictor.py
try:
    sea_level_predictor.predict_sea_level()
  # Exécute la fonction pour générer le graphique
except AttributeError:
    print("Erreur : La fonction 'draw_plot()' n'existe pas dans 'sea_level_predictor.py'.")
    print("Vérifiez le nom de la fonction dans 'sea_level_predictor.py' et modifiez 'main.py' en conséquence.")

# Exécuter les tests unitaires
if __name__ == "__main__":
    main(module='test_module', exit=False)
