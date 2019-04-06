import os
import functools
import re
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import psycopg2


bp = Blueprint('pages', __name__, url_prefix='')


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/results')
def results():
    return render_template('results.html')
