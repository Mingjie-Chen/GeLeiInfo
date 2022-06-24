from myapp import app
from flask import render_template, flash, redirect,url_for
from myapp.forms import LoginForm
from myapp.forms import SignupForm
user = {'username': 'Jack'}
@app.route('/')
@app.route('/base')
def base():
    return render_template('base.html', user=user)
@app.route('/index')
def index():
    return render_template('index.html',title='Home', user=user)
@app.route('/loops')
def post():
    posts = [
        {'author':{'username': 'Abey'},
        'body': 'The Avengers movie was so cool!'
        },
        {
        'author':{'username': 'Sean'},
        'body': 'The All-Blacks win again!'
        }
    ]
    return render_template('loops.html',title='Home',user=user,posts=posts)
        
        
@app.route('/test')
def test():
    return render_template('test.html',title='Home')
    
@app.route('/exe1')
def exe1():
    return render_template('exe1.html',user=user)
    
@app.route('/exe2')
def exe2():
    list=[{ 'username': 'John',
    'saying':'Good Morning'
    },{'username': 'Mary',
    'saying':'Good Riddance'
    },{'username': 'Abey',
    'saying':'I hate python'
    }]
    return render_template('exe2.html',user=user,lists=list)
    
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('login'))
    return render_template('login.html',title='Sign In', form=form)
    
@app.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.password.data!=form.password2.data:
            flash('Passwords do not match')
            return redirect(url_for('signup'))
        user=User(username=form.username.data,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('User registered with username:{}'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('signup.html',title='Register a new user',form=form)
    
    
    
    
    
    
    
    
    