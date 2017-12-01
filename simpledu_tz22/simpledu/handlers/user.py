from flask import Blueprint,render_template
from simpledu.models import User

user=Blueprint('user',__name__,url_prefix='/user')

@user.route('/<username>')
def index(username):
    user1 = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user1=user1)

@user.errorhandler(404)
def not_found(error):
    return render_template('404.html')
