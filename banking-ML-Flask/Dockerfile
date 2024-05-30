# Utilisez l'image de base Python
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers requis dans le conteneur
COPY requirements.txt /app/
COPY app /app/app

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel l'application Flask écoute
EXPOSE 5000

# Commande pour exécuter l'application lorsque le conteneur démarre
CMD ["python", "-m", "app.run"]
