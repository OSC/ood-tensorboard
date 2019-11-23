from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TensorboardForm(FlaskForm):
    logdir = StringField('Log Directory', validators=[DataRequired()])
    submit = SubmitField('Open Tensorboard')
