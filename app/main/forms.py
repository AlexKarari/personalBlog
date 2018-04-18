from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class Blog_PostForm(FlaskForm):

    title = StringField('Blog', validators=[Required()])
    Blog_post = TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Submit')
