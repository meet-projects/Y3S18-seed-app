from flask import (
        Blueprint, redirect, render_template,
        Response, request, url_for
)
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError

from project import db
from project.forms import RegisterForm, LoginForm
from project.models import *

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
        fname= request.form.get('fname')
        lname= request.form.get('lname')
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
                teacher=Teacher(user.id,fname,lname,"undefined yet","undefined yet",0,"undefined yet","","https://static.thenounproject.com/png/214280-200.png","")
                db.session.add(teacher)
                db.session.commit()
                login_user(user, remember=True)

                return redirect(url_for('edit_profile',teacher_id=teacher.id))

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
        return render_template('index.html', loginform=loginform)

@users_bp.route('/login_signup')
def login_signup():
    loginform = LoginForm(request.form)
    return render_template('login_signup.html',loginform=loginform)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.index'))

@users_bp.route('/teacher/<int:teacher_id>')
def profile(teacher_id):
    teacher = db.session.query().filter_by(id=teacher_id).first()
    return render_template('profile_template.html', teacher=teacher)

@users_bp.route('/make_request/<int:teacher_id>', methods=['POST'])
def make_request(teacher_id):
    studentfname=request.form.get('studentfname')
    studentlname=request.form.get('studentlname')
    studentnum=request.form.get('studentnum')
    thisteacher=Teacher.query.filter_by(id=teacher_id).first()
    sid=thisteacher.user_id
    student=Student(sid,studentfname,studentlname,studentnum)
    book=Request(student.id,thisteacher.id,False)
    db.session.add(student)
    db.session.commit()
    db.session.add(book)
    db.session.commit()
    return redirect('feed')


@users_bp.route('/editing/<int:teacher_id>', methods=['POST'])
@login_required
def editing(teacher_id):
    teacher=Teacher.query.filter_by(id=teacher_id).first()
    fname= request.form.get('fname')
    lname= request.form.get('lname')
    city=request.form.get('city')
    fee=request.form.get('fee')
    description=request.form.get('description')
    phone_num=request.form.get('phone_num')
    car_type=request.form.get('car_type')
    arabic=request.form.get('arabic')
    hebrew=request.form.get('hebrew')
    english=request.form.get('english')
    profile_picture=request.form.get('profile_picture')
    automatic=request.form.get('automatic')
    manual=request.form.get('manual')
    if fname!="":
        teacher.fname=fname
    if lname!="":
        teacher.lname=lname
    if city!="":
        teacher.city=city
    if fee=="":
        pass
    else:
        teacher.cost=fee
    if description!="":
        teacher.description=description
    if phone_num!="":
        teacher.phone_num=phone_num
    if car_type!="":
        teacher.car_type=car_type
    if arabic is not None or english is not None or hebrew is not None:
        teacher.languages=""
    if arabic is not None:
        teacher.languages+="Arabic "
    if hebrew is not None:
        teacher.languages+="Hebrew "
    if english is not None:
        teacher.languages+="English "
    if profile_picture!="":
        teacher.profile_picture=profile_picture
    else:
        pass
    if automatic is not None or manual is not None:
        teacher.gearbox=""
    if automatic is not None:
        teacher.gearbox+="Automatic "
    if manual is not None:
        teacher.gearbox+="Manual "
    db.session.commit()
    return redirect('profile_template')
    #else:
    #    teach = Teacher.query.filter_by(id=teacher_id).first()
    #    all_cities = City.query.all()
    #    return render_template('edit_profile_template.html', teacher=teach, all_cities=all_cities)


@users_bp.route('/delete/<int:teacher_id>')
def delete(teacher_id):
    teach=Teacher.query.filter_by(id=teacher_id).first()
    db.session.delete(teach)
    db.session.commit()
    return redirect('/')











###student


@users_bp.route('/teacher/<int:teacher_id>')
def profile(teacher_id):
    teacher = db.session.query().filter_by(id=teacher_id).first()
    return render_template('profile_template.html', teacher=teacher)



@users_bp.route('/student_signup',methods=['GET', 'POST'])
def student_signup():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        password2=request.form.get('password2')
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        phone_num=request.form.get('phone_num')
        if password== password2:
                user = User.query.filter_by(email=email).first()
                if user is None:
                    user=User(email,password,"student")
                    db.session.add(user)
                    db.session.commit()
                    
                    student=Student(fname,lname,phone_num,gearbox,city,min_price,max_price,"")
                    db.session.add(student)
                    db.session.commit()
                    login_user(user, remember=True)
                    return redirect(url_for('filter'))
        else:
            return Response("<p>invalid form</p>")

    return render_template('index.html', form=form)


@users_bp.route('/filter', methods=['GET', 'POST'])
@login_required
def filter():
    student=Student.query.filter_by(user_id=current_user.id).first()
    if student is not None:
        arabic=request.form.get('arabic')
        hebrew=request.form.get('hebrew')
        english=request.form.get('english')
        automatic=request.form.get('automatic')
        manual=request.form.get('manual')
        city=request.form.get('city')
        min_price=request.form.get('min_price')
        max_price=request.form.get('max_price')
        if city!="":
            student.city=city
        if min_price=="":
            pass
        else:
            teacher.min_price=min_price
        if max_price=="":
            pass
        else:
            teacher.max_price=max_price
        if arabic is not None:
            student.languages+="Arabic "
        if hebrew is not None:
            student.languages+="Hebrew "
        if english is not None:
            student.languages+="English "
        if automatic is not None:
            student.gearbox+="Automatic "
        if manual is not None:
            student.gearbox+="Manual "
        db.session.commit()
        return redirect('feed')
    return redirect('feed')
