from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField("Name:", validators=[Required()])
    post = TextAreaField("Description:", validators=[Required()])
    contact = StringField("Email:", validators=[Required()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Name", validators=[Required()])
    post = TextAreaField("Description", validators=[Required()])
    contact = StringField("Email:", validators=[Required()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Review", validators=[Required()])
    alias = StringField("Review Alias")
    submit = SubmitField("Review")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")
