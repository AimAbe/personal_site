# app/routes/portfolio.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, current_user
from app import db
from app.forms import ProjectForm
from app.models import Project  # You'll need to create this model too

portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@portfolio.route("/portfolio")
def portfolio_home():
    projects = Project.query.all()
    return render_template('portfolio/portfolio.html', title='Portfolio', projects=projects)

@portfolio.route("/portfolio/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            technologies=form.technologies.data,
            github_link=form.github_link.data,
            live_link=form.live_link.data,
            image=form.image.data,
            user_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Your project has been added!', 'success')
        return redirect(url_for('portfolio.portfolio_home'))
    return render_template('portfolio/create_project.html', title='New Project', form=form, legend='New Project')

@portfolio.route('/')
def portfolio_list():
    projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('portfolio/list.html', title='Portfolio', projects=projects)

@portfolio.route('/<int:project_id>')
def portfolio_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('portfolio/detail.html', title=project.title, project=project)