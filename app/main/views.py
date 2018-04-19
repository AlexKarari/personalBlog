from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import Blog_PostForm
from ..models import Blog

@main.route('/')
def index():
    form = Blog_PostForm()

    return render_template('blogpost.html', form=form)
