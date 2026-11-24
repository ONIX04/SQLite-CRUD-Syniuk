"""Веб-застосунок «Домашня бібліотека» на Flask: маршрути CRUD."""
from flask import Flask, render_template, request, redirect, url_for, abort

import database_connector as db

app = Flask(__name__)

STATUSES = ["не прочитана", "читаю", "прочитана"]


def form_to_data(form):
    """Збирає дані книги з HTML-форми."""
    def to_int(value):
        return int(value) if value.strip().isdigit() else None

    return {
        "title": form["title"].strip(),
        "author": form["author"].strip(),
        "genre": form.get("genre", "").strip(),
        "year": to_int(form.get("year", "")),
        "pages": to_int(form.get("pages", "")),
        "status": form.get("status", STATUSES[0]),
    }


@app.route("/")
def index():
    """Read: головна сторінка з таблицею всіх книг."""
    return render_template("index.html", books=db.get_all_items())


@app.route("/add", methods=["GET", "POST"])
def add():
    """Create: форма додавання книги."""
    if request.method == "POST":
        db.insert_item(form_to_data(request.form))
        return redirect(url_for("index"))
    return render_template("form.html", book=None, statuses=STATUSES)


@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit(item_id):
    """Update: форма редагування з уже заповненими даними."""
    book = db.get_item_by_id(item_id)
    if book is None:
        abort(404)
    if request.method == "POST":
        db.update_item(item_id, form_to_data(request.form))
        return redirect(url_for("index"))
    return render_template("form.html", book=book, statuses=STATUSES)


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    """Delete: видалення книги і повернення на головну."""
    db.delete_item(item_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_db_table()
    app.run(debug=True)
