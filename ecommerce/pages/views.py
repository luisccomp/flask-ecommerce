from flask import Blueprint, render_template

blueprint = Blueprint('pages', __name__)


@blueprint.route('/')
def home():
    return render_template('home.html', title='Home')


@blueprint.route('/about')
def about():
    return render_template('about.html', title='About')
