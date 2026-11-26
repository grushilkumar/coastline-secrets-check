# Coastline settlement: database secrets

A small service that posts the day's card settlements to the settlement database.

- `app/db.py` reads the database settings and takes the password from the `DB_PASSWORD` environment variable.
- `app/settle.py` marks the day's `READY` settlements as `POSTED`.
- `config/settings.yaml` names the settings; it holds no password.

`.env` and `.pgpass` are a developer's local files that were committed by mistake. Their password is a demo value, not real.
