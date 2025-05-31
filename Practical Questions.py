# 1. How do you create a basic Flask application?
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

# 2. How do you serve static files like images or CSS in Flask?
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# 3. How do you define different routes with different HTTP methods in Flask?
from flask import request

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        return "Handling POST request"
    return "Handling GET request"

# 4. How do you render HTML templates in Flask?
from flask import render_template

@app.route('/home')
def home():
    return render_template('index.html')

# 5. How can you generate URLs for routes in Flask using url_for?
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/profile')
def profile():
    return "User Profile Page"

@app.route('/dashboard')
def dashboard():
    return f"Visit Profile: {url_for('profile')}"

if __name__ == '__main__':
    app.run(debug=True)

# 6. How do you handle forms in Flask?
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

# 7. How can you validate form data in Flask?
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for WTForms

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# 8. How do you manage sessions in Flask?
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session security

@app.route('/set_session')
def set_session():
    session['username'] = 'Shivam'
    return "Session stored!"

@app.route('/get_session')
def get_session():
    return f"Welcome, {session.get('username', 'Guest')}!"

if __name__ == '__main__':
    app.run(debug=True)

# 9. How do you redirect to a different route in Flask?
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/go-to-profile')
def go_to_profile():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return "User Profile Page"

if __name__ == '__main__':
    app.run(debug=True)

# 10. How do you handle errors in Flask (e.g., 404)?
@app.errorhandler(500)
def internal_server_error(error):
    return {"error": "Something went wrong!"}, 500

@app.errorhandler(403)
def forbidden(error):
    return {"error": "Access denied!"}, 403

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 11. How do you structure a Flask app using Blueprints?
from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/profile')
def profile():
    return "User Profile Page"

from flask import Flask
from app.blueprints.user.routes import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)

# 12. How do you define a custom Jinja filter in Flask?
from flask import Flask, render_template

app = Flask(__name__)

#Custom Jinja filter
def uppercase(text):
    return text.upper()

# Register the filter
app.jinja_env.filters['uppercase'] = uppercase

@app.route('/')
def home():
    return render_template('index.html', message="hello, flask!")

if __name__ == '__main__':
    app.run(debug=True)

# 13. How can you redirect with query parameters in Flask?
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/redirect-example')
def redirect_example():
    return redirect(url_for('destination', user='Shivam', role='admin'))

@app.route('/destination')
def destination():
    user = request.args.get('user')
    role = request.args.get('role')
    return f"Redirected! User: {user}, Role: {role}"

if __name__ == '__main__':
    app.run(debug=True)

# 14. How do you return JSON responses in Flask?
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    response = {"message": "Hello, Flask!", "status": "success"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

# 15. How do you capture URL parameters in Flask?
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User Profile: {username}"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/post/<int:post_id>/comment/<comment_id>')
def show_comment(post_id, comment_id):
    return f"Post ID: {post_id}, Comment ID: {comment_id}"