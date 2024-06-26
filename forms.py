from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Length, EqualTo
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("e-Mail", validators=[DataRequired()])
    profile = StringField("Profile", validators=[DataRequired(), URL()])
    passwrod = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=18)])
    confirm_password = PasswordField("Password", validators=[DataRequired(), EqualTo('password', message="Password and confirm must be same!")])
    submit = SubmitField("Sign-Up")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField('e-Mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Sign-In")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired(), Length(min=1, max=255, message="Coment >= 255 char")])
    submit = SubmitField("Post")