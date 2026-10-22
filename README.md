# Flask MVC + MySQL + Docker Compose

Beginner-friendly demo application: add notes in a Flask page and save them in MySQL.

## 1. Requirements
- Docker Engine
- Docker Compose plugin (`docker compose`)
- A terminal

## 2. Configure environment
Copy `.env.example` to `.env`, then change both passwords:
```bash
cp .env.example .env
```

## 3. Build and start
Run from this project directory:
```bash
docker compose up --build -d
docker compose ps

Open http://localhost:5000

## 4. Useful DevOps commands
```bash
docker compose logs -f web       # Flask logs
docker compose logs -f db        # MySQL logs
docker compose exec db mysql -uappuser -p flaskdb
docker compose down              # stop/remove containers and network
docker compose down -v            # DANGER: also deletes MySQL volume/data
```

## 5. How MVC maps to this project
- Model: `app/models/note.py` describes the `notes` database table.
- View: `app/templates/index.html` renders the browser page.
- Controller: `app/controllers/home_controller.py` handles HTTP requests and calls the model.
- App setup: `app/__init__.py` configures Flask and the database connection.

## 6. Multi-stage Dockerfile
- `builder` stage creates dependency wheels.
- `runtime` stage starts from a fresh Python image and installs those wheels.
- Only application files and installed dependencies are kept in the runtime stage, not the builder's build workspace.
- Gunicorn serves the Flask app; Flask's development server is not used in the container.

## 7. Networking and persistence
- Compose creates a private bridge network named for this project.
- Flask connects to host `db`, which is the Compose service name. Do not use `localhost` for the MySQL host from inside Flask.
- `mysql_data` keeps database files when containers are recreated.
- `depends_on` with `service_healthy` waits for MySQL's healthcheck before starting Flask.



## Notes
- This is a learning project, not a production-ready deployment.
- Change the example passwords. For production, use a secrets manager, TLS where appropriate, database migrations, backups, and a non-root runtime user (already configured for Flask).
- `db.create_all()` is convenient for a demo. Use Flask-Migrate/Alembic for schema changes in a real application.
- Notes creation is this project.
