# Installation

$ ./install-kafka.sh

# Console d'accès

```
$ docker run -it --rm  -p 9000:9000 -e ZK_HOSTS="172.17.0.1:2181" -e APPLICATION_SECRET=letmein sheepkiller/kafka-manager
```

Il faut remplacer l'adresse par celle de l'interface docker 
```
ifconfig docker0 | grep "inet " | sed 's/.* inet \(.*\)  netmask.*$/\1/g'
```

# Notes

## ZooKeeper

ZooKeeper joue plusieurs rôles importants dans une architecture microservice.
 - Registry : il stocke les adresses des serveurs
 - Discovery : il permet de trouver les services existants
 - Configuration management : il a une base clé-valeur pour la configuration

## Kafka

### Description

**Apache Kafka** est un système de file de messages

### Concepts

 - Topic
 - Queue

# Annexes

 - https://www.slideshare.net/rahuldausa/introduction-to-kafka-and-zookeeper
