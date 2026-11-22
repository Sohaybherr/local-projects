# 375Scores Football Dashboard

## Overview

A React and Vite football interface with an Express/PostgreSQL API for countries, competitions, teams, players, matches, news, search, and user profiles.

## Academic Objectives

Study the separation of presentation, HTTP routing, domain logic, and relational persistence in a football information system.

## Methodology and Implementation

The React client requests domain resources through an Express REST API. PostgreSQL provides persistence, while Python scripts support data preparation. The development configuration forwards client API requests to the backend.

## Source Organization

- `frontend/`: React views, components, and API adapters.
- `myapp-backend/src/`: server configuration and domain modules.
- `myapp-backend/scripts/`: data preparation utilities.

## Environment and Execution

Requirements: Node.js/npm and PostgreSQL. The backend listens on port 3000.

1. In `myapp-backend`, run `npm ci`.
2. Set `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, and `PGDATABASE` in your shell (see `.env.example`). The Node backend reads shell environment variables; it does not automatically load `.env`.
3. Supply a compatible football database schema, then run `npm start`. No schema migration is included in this snapshot. Optional Python seeding tools require `faker` and `psycopg2-binary`.
4. In `frontend`, run `npm ci`, then `npm run dev`. Vite proxies `/api` requests to the local backend in this upload copy. Run `npm run build` to produce the frontend build.

Database credentials are supplied through environment variables; generated datasets are not distributed. API/database integration has not been exercised.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.
