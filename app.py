from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = "database/tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    os.makedirs("database", exist_ok=True)

    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL DEFAULT 'Medium',
            due_date TEXT,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    connection = get_db_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Medium")
    due_date = request.form.get("due_date", "")

    if not title:
        return redirect(url_for("home"))

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO tasks (title, description, priority, due_date)
        VALUES (?, ?, ?, ?)
        """,
        (title, description, priority, due_date)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        """
        UPDATE tasks
        SET completed = CASE
            WHEN completed = 0 THEN 1
            ELSE 0
        END
        WHERE id = ?
        """,
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))

@app.route("/edit/<int:task_id>")
def edit_task(task_id):
    connection = get_db_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return render_template("edit.html", task=task)

@app.route("/edit/<int:task_id>", methods=["POST"])
def update_task(task_id):
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Medium")
    due_date = request.form.get("due_date", "")

    if not title:
        return redirect(url_for("edit_task", task_id=task_id))

    connection = get_db_connection()

    connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, due_date = ?
        WHERE id = ?
        """,
        (title, description, priority, due_date, task_id)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)