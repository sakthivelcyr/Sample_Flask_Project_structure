from flask import Blueprint
from flask import redirect, url_for, render_template

app_bp = Blueprint("test", __name__)

v = True
# http://localhost:5000/home/auth/
@app_bp.route('/home')
def hello():
    if v:
        return "home"
    else:
        return redirect(url_for('login',name="",id=8))

@app_bp.route('/login_user/<id>/<int:name>')
def login(id):
    name = "test"
    return render_template('index.html', title=name)