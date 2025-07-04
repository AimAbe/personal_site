# app/routes/portfolio.py
from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Project
from app.forms import ProjectForm
from app import db
from flask_login import login_required

portfolio = Blueprint('portfolio', __name__)

@portfolio.route('/portfolio')
def portfolio_list():
    projects = Project.query.order_by(Project.date_added.desc()).all()
    return render_template('portfolio/list.html', title='Portfolio', projects=projects)

@portfolio.route('/portfolio/<int:project_id>')
def portfolio_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('portfolio/detail.html', title=project.title, project=project)

@portfolio.route('/portfolio/new', methods=['GET', 'POST'])
@login_required
def portfolio_create():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            image_url=form.image_url.data,
            project_url=form.project_url.data
        )
        db.session.add(project)
        db.session.commit()
        flash('Your project has been added!', 'success')
        return redirect(url_for('portfolio.portfolio_list'))
    return render_template('portfolio/create.html', title='New Project', form=form)