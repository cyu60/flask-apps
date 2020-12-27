from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

app.config["SECRET_KEY"] = "606f36256c1e65ac6075db285c0b4958"

posts = [
    {
        'author': "Ben",
        'title': "First Title",
        'content': "First Post Content",
        'date_posted': "December 27, 2020"
    },
    {
        'author': "Ben",
        'title': "Second Title",
        'content': "Second Post Content",
        'date_posted': "December 27, 2020"
    },
]

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.", "success")
        return redirect(url_for("home"))

    return render_template('register.html', title="Register", form=form)
    
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)