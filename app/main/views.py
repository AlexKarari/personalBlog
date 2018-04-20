from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import Blog_PostForm
from ..models import Blog
from .. import db
import markdown2

@main.route('/', methods=['GET','POST'])
def index():
    form = Blog_PostForm()

    if form.validate_on_submit():
        title = form.title.data
        Blog_post = form.Blog_post.data

        blog = Blog(blog_name=title, blog_info=Blog_post)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.blogpost'))
    posts = Blog.query.all()
    return render_template('index.html', form=form,posts =posts)

@main.route('/blogpost/', methods=['GET', 'POST'])
def new_blog():
    form = Blog_PostForm()

    if form.validate_on_submit():
        title = form.title.data
        Blog_post = form.Blog_post.data

        blog = Blog(blog_name=title, blog_info=Blog_post)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.index'))
    posts = Blog.query.all()
    return render_template('blogpost.html', form=form, posts=posts)


@main.route('/blog/<int:id>')
def blog(id):
    '''
    View blog page function that returns the posted blogpost
    '''


    blog = Blog.query.get(id)
    title = f'{blog.blog_name}'
    

    return render_template('myposts.html', blog=blog,title =title)

