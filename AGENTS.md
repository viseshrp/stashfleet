# Repository instructions

Stashfleet is a standalone Python library and CLI for server-to-client backups.

- Preserve unrelated work. Stage only intended files; do not commit or push unless requested.
- Keep private `backup.toml`, rclone credentials, SSH keys, backup data, and generated state out of Git and package artifacts. Use sanitized examples.
- Run `uv sync --locked --group dev`, `uv run pytest`, `uv run ruff check .`, and `uv build` for package changes.
- Tests and demos must stay offline and use temporary fixtures. Do not run real backups, cloud uploads, retention deletion, or remote writes without authorization.
- Do not create, enable, or change recurring schedules without explicit approval. Scheduler examples are inert until installed by the operator.
- Preserve source files and existing backup state. File copies do not prove database consistency or a successful restore; report verification limits precisely.
