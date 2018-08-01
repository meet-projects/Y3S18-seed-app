from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for
)
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import User,Teacher,Request, City

users_bp = Blueprint('users', __name__)

@users_bp.route('/')
def index():
    loginform = LoginForm(request.form)
    return render_template('index.html',loginform=loginform)

@users_bp.route('/sign_up', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')
        password2= request.form.get('psw-repeat')
        name= request.form.get('name')
        #city=request.form.get('city')
        #fee=request.form.get('fee')
        #description=request.form.get('description')
        #phonenum=request.form.get('phonenum')
        #car_type=request.form.get('car_type')
        #license_num=request.form.get('license_num')
        #languages_ar=request.form.get('languages_ar')
        #languages_hb=request.form.get('languages_hb')
        #languages_en=request.form.get('languages_en')
        #profilepic=request.form.get('profilepic')
        #lan=""
        if password== password2:
            user = User.query.filter_by(email=email).first()
            if user is None:
                user=User(email,password)
                db.session.add(user)
                db.session.commit()
                #if languages_hb is not None:
                #    lan=lan+"Hebrew "
                #if languages_en is not None:
                #    lan=lan+"English "
                #if languages_ar is not None:
                #    lan=lan+"Arabic "
                #if profilepic == "":
                #    profilepic="https://cdn2.iconfinder.com/data/icons/coach-instructor-trainer-teacher-jobs-occupations-/267/occupation-14-001-512.png"
                #teacher=Teacher(user.id,name,city,description,fee,phonenum,lan,profilepic,gearbox)
                teacher=Teacher(user.id,name,"undefined yet","undefined yet",0,"undefined yet","","undefined yet","")
                db.session.add(teacher)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('editing',teacher_id=teacher.id))

            ##next_page = request.args.get('next')
            ##if not next_page or url_parse(next_page).netloc != '':
               ## next_page = url_for('private_route')
            ##return redirect(next_page)
        else:
            return Response("<p>invalid form</p>")

    return render_template('feed.html', form=form)
                

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm(request.form)
    if request.method == 'POST':
        if loginform.validate_on_submit():
            email = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user is None or not user.check_password(password):
                return Response("<p>Incorrect username or password</p>")
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('profile_template')
            return redirect(next_page)
        else:
            return Response("<p>invalid form</p>")
    else:
        return render_template('login.html', loginform=loginform)

@users_bp.route('/login_signup')
def login_signup():
    loginform = LoginForm(request.form)
    return render_template('login_signup.html',loginform=loginform)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return Response("<p>Logged out</p>")

@users_bp.route('/teacher/<int:teacher_id>')
def profile(teacher_id):
    teacher = db.session.query().filter_by(id=teacher_id).first()
    return render_template('profile_template.html', teacher=teacher)

@users_bp.route('/<int:teacher_id>/booking')
def booking(teacher_id):
    studentname=request.form.get('studentname')
    studentnum=request.form.get('studentnum')
    thisteacher=Teacher.query.filter_by(id=teacher_id).first()
    book=Booking(studentname,studentnum,thisteacher.id,False)
    db.session.add(book)
    db.session.commit()
    return redirect('feed')

# @users_bp.route('/booking/<int:teacher_id>')
# def booking(teacher_id):
#     teacher = db.session.query(Teacher).filter_by(id=teacher_id).first()
#     return render_template('booking.html', teacher=teacher)

@users_bp.route('/editing/<int:teacher_id>', methods=['POST'])
@login_required
def editing(teacher_id):
    teacher=Teacher.query.filter_by(id=teacher_id).first()
    name= request.form.get('name')
    city=request.form.get('city')
    fee=request.form.get('fee')
    description=request.form.get('description')
    phone_num=request.form.get('phone_num')
    car_type=request.form.get('car_type')
    arabic=request.form.get('arabic')
    hebrew=request.form.get('hebrew')
    english=request.form.get('english')
    profilepic=request.form.get('pic')
    automatic=request.form.get('automatic')
    manual=request.form.get('manual')
    if name!="":
        teacher.name=name
    if city!="":
        teacher.city=city
    if fee!=0:
        teacher.cost=fee
    if description!="":
        teacher.description=description
    if phone_num!="":
        teacher.phone_num=phone_num
    if car_type!="":
        teacher.car_type=car_type
    teacher.languages=""
    if arabic is not None:
        teacher.languages+="Arabic "
    if hebrew is not None:
        teacher.languages+="Hebrew "
    if english is not None:
        teacher.languages+="English "
    if profilepic!="":
        teacher.profilepic=profilepic
    teacher.gearbox=""
    if automatic is not None:
        teacher.gearbox+="Automatic "
    if manual is not None:
        teacher.gearbox+="Manual "
    db.session.commit()
    return redirect('profile_template')

        db.session.commit()
        return redirect('profile_template')
    else:
        teach = Teacher.query.filter_by(id=teacher_id).first()
        all_cities = City.query.all()
        return render_template('edit_profile_template.html', teacher=teach, all_cities=all_cities)

