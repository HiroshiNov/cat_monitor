.PHONY: dev pi logs down


dev:
copy .env.dev .env || cp .env.dev .env
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build


pi:
cp .env.pi .env
docker compose -f docker-compose.yml -f docker-compose.pi.yml up -d --build


logs:
docker compose logs -f api


down:
docker compose down