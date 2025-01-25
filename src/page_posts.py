import mako.template
import os.path
import randomdate
import random

srcdir = os.path.dirname(__file__)

def generate_data():
    return {
        'view_count': random.randint(1,50),
        'date': randomdate.gen_randomdate()
    }

def get():

    # discovered what a python dictionary was from stack overflow, figured it seemed best fit for giving
    # each post their specific random view and date data without them all being the exact same
    post_list = [
        {'content': 'IT WORKS!'},
        {'content': 'lalalala lalalalalalalalalalalala lalalalalalalala lalalalalalalalalalalalalalalala lalalalalalalala lalalala'},
        {'content': 'SUP YALL'},
        {'content': 'this website looks straight from the 90s, amirite?'},
        {'content': 'I LOVE WORD WRAP! I LOVE WORD WRAP! I LOVE WORD WRAP! I LOVE WORD WRAP! I LOVE WORD WRAP! I LOVE WORD WRAP! I LOVE WORD WRAP! '},
        {'content': 'SEND CAT PICS 4 FOLLOW'},
        {'content': 'i am an html noob'},
        {'content': 'im running out of fake posts to make up!'},
        {'content': 'HELLO WORLD!'},
        {'content': 'last post, seeya!'},
    ]

    for post in post_list:
        random_data = generate_data()
        post.update(random_data)

    T = mako.template.Template(filename=f"{srcdir}/../html/posts.html")
    return T.render(posts = post_list)
    