# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2019 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import os
import click
from flask import Flask

from src.start.tests import main
from src.start.format import format
from src.start.tests_other import main_other
from src.start.format_other import format_other

app = Flask(__name__)


# the minimal Flask application
@app.route('/sorting')
def index():
    test, total_time = main()
    template = format(test, total_time)
    return f'<div>{template}</div>'


# bind multiple URL for one view function
@app.route('/other')
@app.route('/other-algorithms')
def other():
    dijkstra, floyd, kruskal, prim = main_other()
    template = format_other(dijkstra, floyd, kruskal, prim)
    return f'<h1>{template}</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
