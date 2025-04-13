import sqlite3


class Database:
    """
    Une classe simulant une base de données SQLite pour stocker des utilisateurs.
    """

    def __init__(self, db_path=":memory:"):
        """
        Initialise une connexion à la base de données.

        Args:
            db_path: Chemin vers le fichier de base de données SQLite (par défaut: en mémoire)
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        Établit une connexion à la base de données et crée la table des utilisateurs si elle n'existe pas.

        Returns:
            La connexion à la base de données
        """
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row

        # Création de la table des utilisateurs
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL
        )
        """)
        self.connection.commit()

        return self.connection

    def disconnect(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def add_user(self, username, email):
        """
        Ajoute un utilisateur à la base de données.

        Args:
            username: Nom d'utilisateur (unique)
            email: Adresse e-mail de l'utilisateur

        Returns:
            True si l'ajout est réussi, False sinon
        """
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (?, ?)", (username, email)
            )
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            # L'utilisateur existe déjà
            return False

    def get_user(self, username):
        """
        Récupère un utilisateur par son nom d'utilisateur.

        Args:
            username: Nom d'utilisateur à rechercher

        Returns:
            Dictionnaire contenant les informations de l'utilisateur, ou None si non trouvé
        """
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            return dict(user)
        return None

    def delete_user(self, username):
        """
        Supprime un utilisateur de la base de données.

        Args:
            username: Nom d'utilisateur à supprimer

        Returns:
            True si la suppression est réussie, False si l'utilisateur n'existe pas
        """
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.connection.commit()

        return cursor.rowcount > 0
