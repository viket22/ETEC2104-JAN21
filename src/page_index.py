import mako.template
import os.path
import names
import random

srcdir = os.path.dirname(__file__)


def get():
    n = random.choice(names.namelist)
    T = mako.template.Template(filename=f"{srcdir}/../html/home.html")
    return T.render(randomname=n)