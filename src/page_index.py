import mako.template
import os.path

srcdir = os.path.dirname(__file__)

def get():
    T = mako.template.Template(filename=f"{srcdir}/../html/home.html")
    return T.render()
    
