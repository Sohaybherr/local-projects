#!/usr/bin/env python
"""
Seed the football PostgreSQL database with realistic fake data.

Usage:
    python seed_database.py

Required packages:
    pip install faker psycopg2-binary

Database credentials are read from .env. Supported keys:
    DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
    PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE
    DATABASE_URL
"""

from __future__ import annotations

import os
import random
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import psycopg2
from faker import Faker


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
FAKER = Faker()
RANDOM = random.Random(375)

POSITIONS = ["GK", "CB", "LB", "RB", "CDM", "CM", "CAM", "LW", "RW", "ST"]
POSITION_WEIGHTS = [0.09, 0.18, 0.08, 0.08, 0.09, 0.16, 0.09, 0.08, 0.08, 0.17]

LEAGUES = [
    {
        "name": "Premier League",
        "country": "United Kingdom",
        "api_id": 1001,
        "logo": "/uploads/competitions/premier_league.png",
        "teams": [
            "Manchester City", "Arsenal", "Liverpool", "Chelsea", "Manchester United",
            "Tottenham Hotspur", "Newcastle United", "Aston Villa", "West Ham United",
            "Brighton & Hove Albion", "Everton", "Crystal Palace", "Fulham",
            "Brentford", "Wolverhampton Wanderers", "Nottingham Forest", "Leeds United",
            "Leicester City", "Southampton", "Burnley",
        ],
    },
    {
        "name": "La Liga",
        "country": "Spain",
        "api_id": 1002,
        "logo": "/uploads/competitions/la_liga.png",
        "teams": [
            "Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla", "Real Sociedad",
            "Villarreal", "Athletic Club", "Real Betis", "Valencia", "Celta Vigo",
            "Osasuna", "Getafe", "Mallorca", "Girona", "Rayo Vallecano",
            "Espanyol", "Las Palmas", "Alaves", "Granada", "Real Valladolid",
        ],
    },
    {
        "name": "Serie A",
        "country": "Italy",
        "api_id": 1003,
        "logo": "/uploads/competitions/serie_a.png",
        "teams": [
            "Juventus", "Inter", "AC Milan", "Napoli", "Roma", "Lazio", "Atalanta",
            "Fiorentina", "Bologna", "Torino", "Genoa", "Udinese", "Sassuolo",
            "Empoli", "Cagliari", "Verona", "Parma", "Monza", "Lecce", "Sampdoria",
        ],
    },
    {
        "name": "Bundesliga",
        "country": "Germany",
        "api_id": 1004,
        "logo": "/uploads/competitions/bundesliga.png",
        "teams": [
            "Bayern Munich", "Borussia Dortmund", "Bayer Leverkusen", "RB Leipzig",
            "Eintracht Frankfurt", "Wolfsburg", "Borussia Monchengladbach",
            "Stuttgart", "Freiburg", "Mainz", "Augsburg", "Werder Bremen",
            "Hoffenheim", "Union Berlin", "Koln", "Hamburger SV", "Schalke 04",
            "Hertha Berlin", "Bochum", "Heidenheim",
        ],
    },
    {
        "name": "Ligue 1",
        "country": "France",
        "api_id": 1005,
        "logo": "/uploads/competitions/ligue_1.png",
        "teams": [
            "Paris Saint-Germain", "Marseille", "Lyon", "Monaco", "Lille", "Rennes",
            "Nice", "Lens", "Nantes", "Montpellier", "Strasbourg", "Toulouse",
            "Reims", "Brest", "Lorient", "Metz", "Saint-Etienne", "Auxerre",
            "Angers", "Clermont Foot",
        ],
    },
]


def load_env(path: Path = ENV_PATH) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def connect():
    load_env()

    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return psycopg2.connect(database_url)

    required = {
        "DB_USER or PGUSER": os.getenv("DB_USER") or os.getenv("PGUSER"),
        "DB_PASSWORD or PGPASSWORD": os.getenv("DB_PASSWORD") or os.getenv("PGPASSWORD"),
        "DB_NAME or PGDATABASE": os.getenv("DB_NAME") or os.getenv("PGDATABASE"),
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise RuntimeError(
            "Missing database settings in .env: "
            + ", ".join(missing)
            + ". Add them to myapp-backend/.env or set DATABASE_URL."
        )

    return psycopg2.connect(
        host=os.getenv("DB_HOST") or os.getenv("PGHOST") or "localhost",
        port=int(os.getenv("DB_PORT") or os.getenv("PGPORT") or "5432"),
        user=os.getenv("DB_USER") or os.getenv("PGUSER"),
        password=os.getenv("DB_PASSWORD") or os.getenv("PGPASSWORD"),
        dbname=os.getenv("DB_NAME") or os.getenv("PGDATABASE"),
    )


def table_exists(cursor, table: str) -> bool:
    cursor.execute(
        """
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'public' AND table_name = %s
        )
        """,
        (table,),
    )
    return bool(cursor.fetchone()[0])


def get_columns(cursor, table: str) -> set:
    cursor.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = %s
        """,
        (table,),
    )
    return {row[0] for row in cursor.fetchall()}


def insert_row(cursor, table: str, data: Dict[str, Any], returning: str = "id") -> Optional[int]:
    columns = get_columns(cursor, table)
    filtered = {key: value for key, value in data.items() if key in columns}

    if not filtered:
        raise ValueError(f"No matching columns to insert into {table}")

    names = list(filtered.keys())
    placeholders = ", ".join(["%s"] * len(names))
    column_sql = ", ".join(names)
    values = [filtered[name] for name in names]

    if returning in columns:
        query = f"INSERT INTO {table} ({column_sql}) VALUES ({placeholders}) RETURNING {returning}"
        cursor.execute(query, values)
        return cursor.fetchone()[0]

    query = f"INSERT INTO {table} ({column_sql}) VALUES ({placeholders})"
    cursor.execute(query, values)
    return None


def find_one_id(cursor, table: str, column: str, value: Any) -> Optional[int]:
    columns = get_columns(cursor, table)
    if column not in columns:
        return None

    cursor.execute(f"SELECT id FROM {table} WHERE {column} = %s LIMIT 1", (value,))
    row = cursor.fetchone()
    return row[0] if row else None


def get_country_id(cursor, country_name: str) -> int:
    cursor.execute("SELECT id FROM countries WHERE LOWER(name) = LOWER(%s) LIMIT 1", (country_name,))
    row = cursor.fetchone()
    if row:
        return row[0]

    cursor.execute("SELECT id FROM countries WHERE name ILIKE %s LIMIT 1", (f"%{country_name}%",))
    row = cursor.fetchone()
    if row:
        return row[0]

    raise RuntimeError(f"Country not found in countries table: {country_name}")


def seed_competitions(conn) -> List[Dict[str, Any]]:
    print("Seeding competitions...")
    cursor = conn.cursor()
    competitions: List[Dict[str, Any]] = []

    try:
        for league in LEAGUES:
            existing_id = find_one_id(cursor, "competitions", "api_id", league["api_id"])
            country_id = get_country_id(cursor, league["country"])

            if existing_id:
                competition_id = existing_id
            else:
                competition_id = insert_row(
                    cursor,
                    "competitions",
                    {
                        "api_id": league["api_id"],
                        "name": league["name"],
                        "logo": league["logo"],
                        "country_id": country_id,
                        "country": league["country"],
                        "type": "League",
                    },
                )

            competitions.append({**league, "id": competition_id, "country_id": country_id})

        conn.commit()
        return competitions
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def ensure_season(conn) -> Optional[int]:
    cursor = conn.cursor()
    try:
        if not table_exists(cursor, "seasons"):
            return None

        columns = get_columns(cursor, "seasons")
        if "name" in columns:
            cursor.execute("SELECT id FROM seasons WHERE name = %s LIMIT 1", ("2026/27",))
            row = cursor.fetchone()
            if row:
                return row[0]

        data = {
            "name": "2026/27",
            "year": 2026,
            "start_date": date(2026, 8, 1),
            "end_date": date(2027, 5, 31),
        }
        season_id = insert_row(cursor, "seasons", data)
        conn.commit()
        return season_id
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def short_name(team_name: str) -> str:
    words = [word for word in team_name.replace("&", "").split() if word.lower() not in {"fc", "cf"}]
    return " ".join(words[:2])[:20]


def team_code(team_name: str) -> str:
    letters = "".join(word[0] for word in team_name.replace("&", "").split() if word)
    return (letters[:3] or team_name[:3]).upper()


def seed_teams(conn, competitions: Sequence[Dict[str, Any]], season_id: Optional[int]) -> List[Dict[str, Any]]:
    print("Seeding teams...")
    cursor = conn.cursor()
    teams: List[Dict[str, Any]] = []

    try:
        api_id = 2000
        for competition in competitions:
            for name in competition["teams"]:
                api_id += 1
                existing_id = find_one_id(cursor, "teams", "api_id", api_id)
                logo_name = name.lower().replace(" ", "_").replace("&", "and").replace(".", "")
                team_data = {
                    "api_id": api_id,
                    "competition_id": competition["id"],
                    "country_id": competition["country_id"],
                    "country": competition["country"],
                    "name": name,
                    "short_name": short_name(name),
                    "code": team_code(name),
                    "founded": RANDOM.randint(1870, 1999),
                    "stadium": f"{name} Stadium",
                    "logo": f"/uploads/teams/{logo_name}.png",
                }

                team_id = existing_id or insert_row(cursor, "teams", team_data)
                teams.append({**team_data, "id": team_id})

                if season_id and table_exists(cursor, "team_competitions"):
                    cursor.execute(
                        """
                        SELECT id FROM team_competitions
                        WHERE team_id = %s AND competition_id = %s AND season_id = %s
                        LIMIT 1
                        """,
                        (team_id, competition["id"], season_id),
                    )
                    if not cursor.fetchone():
                        insert_row(
                            cursor,
                            "team_competitions",
                            {
                                "team_id": team_id,
                                "competition_id": competition["id"],
                                "season_id": season_id,
                            },
                        )

        conn.commit()
        return teams
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def weighted_position() -> str:
    return RANDOM.choices(POSITIONS, weights=POSITION_WEIGHTS, k=1)[0]


def seed_players(conn, teams: Sequence[Dict[str, Any]], target_count: int = 2500) -> List[Dict[str, Any]]:
    print("Seeding players...")
    cursor = conn.cursor()
    players: List[Dict[str, Any]] = []

    try:
        api_id = 5000
        per_team = max(1, target_count // len(teams))
        remainder = target_count - (per_team * len(teams))

        for index, team in enumerate(teams):
            count = per_team + (1 if index < remainder else 0)
            for _ in range(count):
                api_id += 1
                existing_id = find_one_id(cursor, "players", "api_id", api_id)
                first_name = FAKER.first_name_male()
                last_name = FAKER.last_name()
                position = weighted_position()
                birth = FAKER.date_between(start_date="-38y", end_date="-17y")
                height = RANDOM.randint(178, 198) if position == "GK" else RANDOM.randint(165, 194)
                weight = max(62, int((height - 100) * RANDOM.uniform(0.78, 0.95)))

                player_data = {
                    "api_id": api_id,
                    "country_id": team["country_id"],
                    "current_team_id": team["id"],
                    "team_id": team["id"],
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": f"{first_name} {last_name}",
                    "birth_date": birth,
                    "nationality": team.get("country"),
                    "height": height,
                    "weight": weight,
                    "position": position,
                    "photo": f"/uploads/players/player_{api_id}.png",
                }

                player_id = existing_id or insert_row(cursor, "players", player_data)
                players.append({**player_data, "id": player_id})

        conn.commit()
        return players
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def score_for_status(status: str) -> Tuple[int, int]:
    if status == "Scheduled":
        return 0, 0
    home = RANDOM.choices([0, 1, 2, 3, 4, 5], weights=[10, 27, 30, 20, 9, 4], k=1)[0]
    away = RANDOM.choices([0, 1, 2, 3, 4, 5], weights=[18, 32, 27, 15, 6, 2], k=1)[0]
    return home, away


def seed_matches(
    conn,
    competitions: Sequence[Dict[str, Any]],
    teams: Sequence[Dict[str, Any]],
    season_id: Optional[int],
    target_count: int = 1500,
) -> List[Dict[str, Any]]:
    print("Seeding matches...")
    cursor = conn.cursor()
    matches: List[Dict[str, Any]] = []

    try:
        teams_by_competition: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
        for team in teams:
            teams_by_competition[team["competition_id"]].append(team)

        start = date(2026, 8, 1)
        end = date(2027, 5, 31)
        today = date.today()
        api_id = 9000

        for competition in competitions:
            league_teams = teams_by_competition[competition["id"]]
            round_robin_pairs = [
                (home, away)
                for home in league_teams
                for away in league_teams
                if home["id"] != away["id"]
            ]
            RANDOM.shuffle(round_robin_pairs)

            league_target = target_count // len(competitions)
            for i, (home, away) in enumerate(round_robin_pairs[:league_target]):
                api_id += 1
                match_date = start + timedelta(days=(i * 3 + RANDOM.randint(0, 2)) % ((end - start).days + 1))
                if match_date < today:
                    status = "Finished"
                elif match_date == today:
                    status = "Live"
                else:
                    status = "Scheduled"
                home_score, away_score = score_for_status(status)

                match_data = {
                    "api_id": api_id,
                    "competition_id": competition["id"],
                    "season_id": season_id,
                    "home_team": home["id"],
                    "away_team": away["id"],
                    "home_team_id": home["id"],
                    "away_team_id": away["id"],
                    "match_date": match_date,
                    "status": status,
                    "match_status": status,
                    "home_score": home_score,
                    "away_score": away_score,
                    "home_goals": home_score,
                    "away_goals": away_score,
                }
                match_id = insert_row(cursor, "matches", match_data)
                matches.append({**match_data, "id": match_id})

        conn.commit()
        return matches
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def seed_news(conn, teams: Sequence[Dict[str, Any]], target_count: int = 300) -> None:
    print("Seeding news...")
    cursor = conn.cursor()

    topics = [
        "transfer update", "injury concern", "match preview", "match report", "press conference",
    ]
    templates = [
        "{team} are preparing for a major {topic} as the football calendar intensifies.",
        "{team} supporters reacted strongly after the latest {topic} from the club camp.",
        "Sources close to {team} expect more details following today's {topic}.",
        "{team} remain focused as coaches assess the squad before another important fixture.",
    ]

    try:
        if not table_exists(cursor, "news"):
            conn.commit()
            return

        cursor.execute("SELECT COUNT(*) FROM news")
        if cursor.fetchone()[0] >= target_count:
            conn.commit()
            return

        for index in range(1, target_count + 1):
            team = RANDOM.choice(teams)["name"]
            topic = RANDOM.choice(topics)
            title = f"{team}: {topic.title()}"
            content = " ".join(
                FAKER.paragraph(nb_sentences=3) for _ in range(3)
            )
            content = f"{RANDOM.choice(templates).format(team=team, topic=topic)} {content}"
            published_at = datetime.now() - timedelta(days=RANDOM.randint(0, 120), hours=RANDOM.randint(0, 23))

            insert_row(
                cursor,
                "news",
                {
                    "title": title,
                    "content": content,
                    "image": f"/uploads/news/news_{index}.png",
                    "published_at": published_at,
                },
            )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def seed_users(conn, target_count: int = 50) -> None:
    print("Seeding users...")
    cursor = conn.cursor()

    try:
        for index in range(1, target_count + 1):
            username = f"{FAKER.user_name()}_{index}"
            email = f"user{index}@example.com"

            if find_one_id(cursor, "users", "email", email):
                continue

            insert_row(
                cursor,
                "users",
                {
                    "username": username,
                    "email": email,
                    "password": f"$2b$12$hashed_placeholder_user_{index}",
                    "profile_picture": f"/uploads/users/user_{index}.png",
                },
            )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def main() -> None:
    conn = connect()
    try:
        competitions = seed_competitions(conn)
        season_id = ensure_season(conn)
        teams = seed_teams(conn, competitions, season_id)
        seed_players(conn, teams)
        seed_matches(conn, competitions, teams, season_id)
        seed_news(conn, teams)
        seed_users(conn)
        print("Database seeded successfully.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
