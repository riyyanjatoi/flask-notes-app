
import os
import time

import psycopg
from psycopg.rows import dict_row
from flask import Flask, jsonify, request

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

MAX_RETRIES = 10
RETRY_DELAY = 2


def get_db_connection():
    return psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row
    )


def initialize_database():
    """Connect to PostgreSQL and create the notes table."""

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS notes (
                            id BIGSERIAL PRIMARY KEY,
                            content TEXT NOT NULL,
                            created_at TIMESTAMPTZ DEFAULT NOW()
                        );
                    """)

            print("Database connected. Notes table is ready.")
            return

        except psycopg.OperationalError as error:
            print(
                f"Database connection attempt "
                f"{attempt}/{MAX_RETRIES} failed: {error}"
            )

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

    raise RuntimeError("Could not connect to PostgreSQL.")


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask Notes App!"


@app.route("/notes", methods=["GET"])
def get_notes():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, content FROM notes ORDER BY id;"
            )
            notes = cur.fetchall()

    return jsonify(notes)


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body is required"}), 400

    content = data.get("content")

    if not isinstance(content, str) or not content.strip():
        return jsonify({"error": "Note content is required"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO notes (content)
                VALUES (%s)
                RETURNING id, content;
                """,
                (content.strip(),)
            )
            note = cur.fetchone()

    return jsonify(note), 201


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    initialize_database()

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=False
    )
