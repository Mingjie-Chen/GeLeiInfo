from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields.core import StringField, IntegerField, DecimalField, SelectField, DateField
from wtforms.fields.simple import PasswordField, SubmitField, FileField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo

render_kw = {'class': 'form-control'}

# 这里对video的form进行了修改，增加了file的name
class VideoUploadForm(FlaskForm):
    file = FileField('Video',validators=[FileRequired()])
    name = StringField('File Name:', validators=[DataRequired()], default = 'Video')
    language = SelectField(('Language'), validators=[DataRequired()],
                         choices=[('English', 'English'), ('Chinese', 'Chinese')], default='English')
    mode = SelectField(('Mode'), validators=[DataRequired()],
                         choices=[('API', 'API'), ('NLP Model', 'Model')], default='API')
    submit = SubmitField('Upload')


