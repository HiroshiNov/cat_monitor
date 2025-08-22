# cat-watch (scaffold)


Windows で開発（ホットリロード）、Raspberry Pi で検証（常時稼働）を同一コードで回すための最小雛形。


## Quick Start


### 1) Windows (dev, hot reload)
```bash
copy .env.dev .env
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
'''
Open: http://localhost:8000

### 2) Raspberry Pi (prod)
```bash
cp .env.pi .env
docker compose -f docker-compose.yml -f docker-compose.pi.yml up -d --build
'''
Open: http://localhost:8000

```bash
Logs: docker compose logs -f api
```bash

