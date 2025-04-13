# Commandes pour utiliser l'application

## Préparation et installation

```bash
# Activer l'environnement virtuel (si ce n'est pas déjà fait)
source venv/bin/activate  # Sur Linux/MacOS
# ou
venv\Scripts\activate     # Sur Windows

# Installer les dépendances (si ce n'est pas déjà fait)
pip install pytest pytest-cov pytest-mock flask requests
```

## Démarrer l'application

```bash
# Démarrer le serveur Flask
python run.py
```

L'application démarrera sur http://127.0.0.1:5000 par défaut.

## Utiliser l'API

Vous pouvez interagir avec l'API via curl ou un navigateur :

### Calculatrice

```bash
# Addition (2 + 3)
curl http://127.0.0.1:5000/api/add/2/3

# Soustraction (5 - 2)
curl http://127.0.0.1:5000/api/subtract/5/2

# Multiplication (4 * 3)
curl http://127.0.0.1:5000/api/multiply/4/3

# Division (10 / 2)
curl http://127.0.0.1:5000/api/divide/10/2
```

### Gestion des utilisateurs

```bash
# Ajouter un utilisateur
curl -X POST http://127.0.0.1:5000/api/user \
  -H "Content-Type: application/json" \
  -d '{"username":"test_user", "email":"user@example.com"}'

# Récupérer un utilisateur
curl http://127.0.0.1:5000/api/user/test_user

# Supprimer un utilisateur
curl -X DELETE http://127.0.0.1:5000/api/user/test_user
```

## Exécuter les tests (après les avoir écris 😜)

```bash
# Exécuter tous les tests
pytest

# Exécuter les tests avec un rapport de couverture
pytest --cov=app

# Exécuter les tests avec un rapport de couverture détaillé
pytest --cov=app --cov-report=html

# Exécuter uniquement les tests du calculateur
pytest tests/test_calculator.py

# Exécuter uniquement les tests de l'API
pytest tests/test_api.py

# Exécuter uniquement les tests de la base de données
pytest tests/test_database.py
```

Pour consulter le rapport de couverture HTML, ouvrez le fichier `htmlcov/index.html` dans votre navigateur après avoir exécuté la commande avec l'option `--cov-report=html`.