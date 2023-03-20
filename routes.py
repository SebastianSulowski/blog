# blog/routes.py

from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm


def create_or_edit_entry(entry_id=None):
    if entry_id:
        entry = Entry.query.filter_by(id=entry_id).first()
        form = EntryForm(obj=entry)
    else:
        form = EntryForm()

    if request.method == 'POST' and form.validate_on_submit():
        if entry_id:
            entry.title = form.title.data
            entry.body = form.body.data
            entry.is_published = form.is_published.data
            db.session.commit()
        else:
            entry = Entry(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
            )
            db.session.add(entry)
            db.session.commit()
        return redirect(url_for('index'))

    return render_template("entry_form.html", form=form)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    return create_or_edit_entry()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    return create_or_edit_entry(entry_id)
