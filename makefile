.PHONY: all up venv run

all: up activate_env run

up:
	cd auth-service/backend && docker compose up -d

venv:
    source auth-service/backend/app/venv/bin/activate
run:
	cd auth-service/backend/app && python3 main.py
