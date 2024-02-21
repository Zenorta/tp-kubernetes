## Info Pratique

Adresse email intervenant: amnay.m@gmail.com

## Préparation

Avant de commencer, assurez-vous de disposer des éléments suivants:

- Compte Google (si vous avez une boîte mail Gmail, c'est tout bon!)
- Compte GitHub
- Compte Docker Hub
- Repo GitHub créé: "tp-kubernetes"

Si vous n'êtes pas familier avec Git, suivez ce [tutoriel](lien-vers-le-tutoriel) pour les bases.

Renseignez vos informations sur [ce Google Sheet](lien-vers-le-sheet).

## TP 1: Microservice HTTP "motd-api"

- Écrivez un microservice HTTP "motd-api" qui retourne toujours un objet JSON {"message": MESSAGE}.
- Le MESSAGE doit être configurable.
- Le service prend deux variables d'environnement pour sa configuration: 
  - MESSAGE est le message retourné par l'API.
  - APP_PORT est le port d'écoute de l'API.

```bash
APP_PORT=5555 MESSAGE="Hello World!" ./motd-api
```

Poussez votre code dans votre dépôt Git.

## TP 2: Dockerisation de "motd-api"

Fournissez le Dockerfile dans le dépôt Git.

## TP 3: Pousser l'image Docker dans Docker Hub

```bash
docker login # Authentification nécessaire au moins une fois
docker build -t <COMPTE_DOCKER_HUB>/<NOM_IMAGE_DOCKER>:<VERSION> .
docker push <COMPTE_DOCKER_HUB>/<NOM_IMAGE_DOCKER>:<VERSION>
```

Documentez le nom de l'image dans le README du dépôt Git.

## TP 4: Installation de gcloud et kubectl

⚠️ Utilisez l'adresse Gmail fournie pour l'authentification GCloud.

- Installez l'outil CLI GCloud: [Guide d'installation](https://cloud.google.com/sdk/docs/install).
- Téléchargez le client Kubernetes kubectl: [Guide d'installation](https://kubernetes.io/docs/tasks/tools/).
- Vérifiez l'installation de kubectl:

```bash
kubectl version
```

Bonus: Activez l'auto-complétion Bash pour kubectl:

```bash
echo 'source <(kubectl completion bash)' >>~/.bashrc
```

ℹ️ Kubectl est votre compagnon pour toute interaction avec un cluster K8S. Voici un [Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) qui peut vous être utile.

## TP 5: Setup de gcloud et kubectl

### Configuration de GCloud

- Authentification:

```bash
gcloud auth login
```

- Notre projet Google Cloud s'appelle "tp-kubernetes-414717":

```bash
gcloud config set project tp-kubernetes-414717
```

- Liste des clusters Kubernetes:

```bash
gcloud container clusters list
```

- Récupérer les credentials de connexion au Cluster Kubernetes:

```bash
export USE_GKE_GCLOUD_AUTH_PLUGIN=True
gcloud container clusters get-credentials --zone=europe-west4-b tp-kubernetes
```

### Kubectl

- Vérifiez que vous avez bien un nouveau contexte K8S:

```bash
kubectl config get-contexts
```

- Vérifiez la communication avec le serveur API du cluster Kubernetes:

```bash
kubectl version
kubectl get nodes
```