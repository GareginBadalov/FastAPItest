THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up start down destroy stop restart logs logs-api ps login-timescale login-api db-shell
build:
	docker-compose -f docker-compose.yml build 
up:
	docker-compose -f docker-compose.yml up -d && docker exec -it  fastapitest-app-1 poetry run alembic upgrade head
start:
	docker-compose -f docker-compose.yml start
down:
	docker-compose -f docker-compose.yml down
destroy:
	docker-compose -f docker-compose.yml down -v
stop:
	docker-compose -f docker-compose.yml stop
restart:
	docker-compose -f docker-compose.yml stop
	docker-compose -f docker-compose.yml up -d
