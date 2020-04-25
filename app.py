from flask import Flask,render_template,request,redirect,url_for,session
from models import User,Question
import config
from exts import db
from decorators.decorators import login_required

app = Flask(__name__)

app.config.from_object(config)

app.DEBUG=True
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def index():
    context = {
        'questions' :Question.query.order_by('-create_time').all()
    }
    return  render_template('index.html',**context)

@app.route('/dasd')
def indexasdas():
    context = {
        'questions' :Question.query.order_by('-create_time').all()
    }
    return  render_template('index.html',**context)



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone_number = request.form.get('phonenumber')
        password = request.form.get('password')

        user = User.query.filter(User.phonenumber == phone_number, User.password == password).first()
        if user:
            session['user_id'] = user.id
            # 如果想在31天内都不需要在登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码活密码错误'


@app.route('/logout/' )
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))




@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return  render_template('regist.html')
    else:
        phone_number = request.form.get('phonenumner')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if  User.query.filter(User.phonenumber == phone_number).first():
            return u'already regist!!!'
        else:
            if password1 != password2:
                return u'other equal'
            else:
                user = User(phonenumber=phone_number,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/question/' , methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user :
            return {'user':user}
    return {}
##AssertionError: The sqlalchemy extension was not registered to the current a
##重中之中
db.init_app(app)
if __name__ == '__main__':

    app.run(debug=True)
