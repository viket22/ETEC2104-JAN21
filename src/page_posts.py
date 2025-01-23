import mako.template
import os.path
import randomdate
import random

srcdir = os.path.dirname(__file__)

def get():
    T = mako.template.Template(filename=f"{srcdir}/../html/posts.html")
    return T.render(randomdate=randomdate.gen_randomdate(),
                     randomviews=random.randint(0,50))
    