from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.simple import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email, length


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
    # 이미지 파일을 받을수있도록 경로 지정
    image = FileField('이미지 업로드', validators=[FileAllowed(['jpg', 'jpeg', 'png','gif'], '이미지 파일만 업로드 가능합니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

# // 회원 가입 폼 모듈
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름',validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', message='비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
#  로그인 폼 모듈
class UserLoginForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired('아이디를 입력해주세요'), Length(min=3, max=25)])
    password = PasswordField('', validators=[DataRequired('비밀번호를 입력해주세요')])