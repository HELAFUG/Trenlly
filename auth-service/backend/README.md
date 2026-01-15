# Auth Service

This is an authentication service built using FastAPI, which provides user registration, login, and management functionalities. The service is containerized using Docker and Docker Compose, and it uses PostgreSQL as the database.

## Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Role-based Access Control
- Dockerized for easy deployment

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework for building APIs.
- [Docker](https://www.docker.com/) - Containerization platform.
- [Docker Compose](https://docs.docker.com/compose/) - Tool for defining and running multi-container Docker applications.
- [PostgreSQL](https://www.postgresql.org/) - Relational database management system.

## Getting Started

### Prerequisites

- Python
- Docker
- Docker Compose

### Clone the Repository

```bash
python -c 'import secrets; print(secrets.token_hex())' # to generate a secrects token
