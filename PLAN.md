## ------- Tests Automatisés ------- ##

Au préalable, dans ton terminal, crée un répertoire tests-automatises-tp1 dans lequel tu travailleras tout au long de ces questions.
Dans ce répertoire, crée un fichier reponses.md (au format MarkDown) qui contiendra les réponses à chaque question ainsi qu'une explication si nécessaire ou demandée (cf "Que constates-tu ?").

### --------------------------------------------- 

## Découverte du projet

Le projet est une application Flask exposant une API REST avec deux fonctionnalités
principales :
    - Une calculatrice capable d'effectuer des opérations basiques :
    addition, soustraction, multiplication, division
    - Un gestionnaire d'utilisateurs permettant d'ajouter, consulter et supprimer des utilisateurs

### --------------------------------------------- 

## Structure du projet

tests-automatises/
├── app/
│ ├── __init__.py # Configuration de l'application Flask
│ ├── api.py # Routes API
│ ├── calculator.py # Classe Calculator avec les opérations mathématiques
│ └── database.py # Classe Database pour la gestion des utilisateurs
├── tests/ # Dossier où vous écrirez vos tests
├── run.py # Script pour lancer l'application
└── README.md # Documentation du projet

### --------------------------------------------- 

## Tester le bon fonctionnement de l'application

Démarrez l'application : python run.py

Testez quelques endpoints pour vérifier que tout fonctionne :

# Test de la calculatrice
curl http://127.0.0.1:5000/api/add/2/3

# Test de la gestion utilisateur
curl -X POST http://127.0.0.1:5000/api/user \
-H "Content-Type: application/json" \
-d '{"username":"test_user", "email":"user@example.com"}'

### --------------------------------------------- 

## Travail à réaliser

# Partie 1 : Tests unitaires
Créez les fichiers de test suivants dans le dossier `tests/` :
1. test_calculator.py: Tests unitaires pour la classe Calculator
    - Testez chaque opération (add, subtract, multiply, divide)
    - Incluez des tests pour les cas limites (division par zéro, etc.)
2. test_database.py: Tests unitaires pour la classe Database
    - Testez les méthodes add_user, get_user, delete_user
    - Utilisez les fixtures pytest pour initialiser et nettoyer la base de données

# Partie 2 : Tests d'intégration
1. test_api.py: Tests d'intégration pour les endpoints de l'API
    - Utilisez le client de test Flask pour simuler des requêtes HTTP
    - Testez les endpoints de calculatrice et de gestion utilisateurs
    - Vérifiez les codes de retour HTTP et le format des réponses JSON

# Partie 3 : Mocks et tests avancés
1. Utilisation de mocks :
    - Modifiez certains tests pour utiliser des mocks (pytest-mock)
    - Simulez le comportement de la base de données pour des tests isolés
2. Analyse de couverture :
    - Exécutez les tests avec génération de rapport de couverture
    - Identifiez les parties de code non couvertes
    - Complétez vos tests pour améliorer la couverture

### --------------------------------------------- 

## Exécution des tests

# Exécuter tous les tests
pytest
# Exécuter les tests avec rapport de couverture
pytest --cov=app
# Générer un rapport de couverture HTML détaillé
pytest --cov=app --cov-report=html
# Exécuter des tests spécifiques
pytest tests/test_calculator.py
pytest tests/test_api.py
pytest tests/test_database.py
