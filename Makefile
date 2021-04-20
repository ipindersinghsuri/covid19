CURRENT_DIR := ${CURDIR}

build-image:
	docker build -f covid19/Dockerfile covid19/ -t ipindersinghsuri/iptest:latest

run-image:
	docker run --rm --network="host" --env DB_NAME=covid19 --env DB_USER=postgres --env DB_PASSWORD=mysecretpassword --env DB_HOST="0.0.0.0" --env DB_PORT="5432" ipindersinghsuri/iptest:latest
