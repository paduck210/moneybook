from flask import (
    redirect,
    render_template,
    request,
    flash,
    url_for
    )
from app import app, db
from app.models import Usage, User, Receipt
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import RegistrationForm, ReceiptForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ReceiptForm()
    receipts = Receipt.query.filter_by(user_id=current_user.id).all()

    if form.validate_on_submit():
        if Usage.query.filter_by(name=form.usage.data).first():
            usage = Usage.query.filter_by(name=form.usage.data).first()
            receipt = Receipt(description=form.description.data, amount=form.amount.data, user_id=current_user.id, usage_id=usage.id)
            db.session.add(receipt)
            db.session.commit()
            flash("New Receipt Added")
        else:
            usage = Usage(name=form.usage.data)
            db.session.add(usage)
            db.session.commit()
            receipt = Receipt(description=form.description.data, amount=form.amount.data, user_id=current_user.id, usage_id=usage.id)
            db.session.add(receipt)
            db.session.commit()
            flash("New Receipt Added")
        return redirect('/index')

    return render_template('index.html', form=form, receipts=receipts)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_POST():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()

    if user is None:
        flash("There is no username [{}]".format(username))
        return redirect('/login')

    if not user.check_password(password):
        flash("Password is incorrect")
        return redirect('/login')

    login_user(user)
    return redirect('/index')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username= form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrat! you are now a new user of blog')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
