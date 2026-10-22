from flask import Blueprint, redirect, render_template, request, url_for
from app import db
from app.models.note import Note

home = Blueprint("home", __name__)

@home.route("/", methods=["GET"])
def index():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template("index.html", notes=notes)

@home.route("/notes", methods=["POST"])
def create_note():
    title = request.form.get("title", "").strip()
    if title:
        db.session.add(Note(title=title))
        db.session.commit()
    return redirect(url_for("home.index"))

@home.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200
