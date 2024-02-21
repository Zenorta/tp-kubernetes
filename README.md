# TP Kubernetes RT0903 - Thibaud PATÉ

## Info Pratique

Adresse mail du développeur : thibaud.pate@gmail.com

## Installation du projet

Le projet se situe dans un docker dont l'image est : zenorta/motd-api

La commande pour récupérer le docker est celle-ci : 
```
docker pull zenorta/motd-api
```


Il faut ensuite utiliser la commande : 

```
kubectl apply -f k8s/
```

## Accès aux données

Pour accéder au pod, voici le lien : 

```
http://thibaud-pate.amnay.fr/motd
```
