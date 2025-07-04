# app/routes/blog.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import BlogPost
from app.forms import BlogPostForm
from app import db
from flask_login import current_user, login_required

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blog_list():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog/list.html', title='Blog', posts=posts)

@blog.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog/detail.html', title=post.title, post=post)

@blog.route('/blog/new', methods=['GET', 'POST'])
@login_required
def blog_create():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog.blog_list'))
    return render_template('blog/create.html', title='New Post', form=form)