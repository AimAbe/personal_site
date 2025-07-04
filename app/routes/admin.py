# app/routes/admin.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.forms import BlogPostForm, ProjectForm
from app.models import BlogPost, Project
from app import db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('admin/blog_form.html', form=form)

@bp.route('/portfolio/new', methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            image_url=form.