from flask import Blueprint, redirect, url_for
from pybo.models import Question

# 블루 프린트: 라우팅 함수를 관리하는 역할
bp = Blueprint('main',__name__, url_prefix='/')


@bp.route('/')  # 라우팅 함수
def index():
   return redirect(url_for('question._list'))
