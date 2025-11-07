# Redis Key-Value Demo (FastAPI + Redis)

Une petite application Python/Redis pour illustrer le modèle clé–valeur et les opérations simples : incrément, cache, file de logs.

## Démarrage rapide

1) Installez Docker Desktop ou équivalent.
2) Depuis le dossier du projet, exécutez :

    docker compose up --build

Application: http://localhost:8000
Statistiques: http://localhost:8000/stats

## Structure des clés Redis

- visits:global (Counter) : compteur de visites
- last_ip (String) : IP du dernier visiteur (TTL 5 min)
- events:visits (List) : derniers événements de connexion

## Objectifs pédagogiques

- Comprendre le modèle clé–valeur Redis
- Manipuler les structures de données simples (string, list)
- Visualiser l’accès concurrent (atomicité des incréments)
- Montrer la simplicité du déploiement Docker
