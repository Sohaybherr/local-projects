# 375Scores Football Dashboard

A React and Vite football interface with an Express/PostgreSQL API for countries, competitions, teams, players, matches, news, search, and user profiles.

## Usage

Requirements: Node.js/npm and PostgreSQL. The backend listens on port 3000.

1. In `myapp-backend`, run `npm ci`.
2. Set `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, and `PGDATABASE` in your shell (see `.env.example`). The Node backend reads shell environment variables; it does not automatically load `.env`.
3. Supply a compatible football database schema, then run `npm start`. No schema migration is included in this snapshot. Optional Python seeding tools require `faker` and `psycopg2-binary`.
4. In `frontend`, run `npm ci`, then `npm run dev`. Vite proxies `/api` requests to the local backend in this upload copy. Run `npm run build` to produce the frontend build.

The local database password and generated datasets were excluded. API/database integration has not been exercised.
