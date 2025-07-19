from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, current_user
from config import Config
from db import db, Task, User
from auth import auth

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)

@app.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
@login_required
def add():
    description = request.form.get('task')
    if description:
        new_task = Task(description=description, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
@login_required
def delete(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)