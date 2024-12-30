# Utiliser l'image Python 3.11 slim (systeme d'exploitation léger installé avec python)
FROM python:3.11-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier requirements
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie de l'ensemble du code dans le répertoire de travail
COPY . .

# Exposition du port utilisé par Flask (Google Cloud utilise généralement le port 8080)
EXPOSE 8080

# Commande pour lancer l'application Flask
CMD ["waitress-serve", "--host=0.0.0.0", "--port=8080", "main:app"]
