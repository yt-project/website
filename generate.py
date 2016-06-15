import yaml
import os
from jinja2 import Environment, FileSystemLoader
import hglib
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

pages = {}

def page(name):
    def _page(func):
        pages[name] = (func, name + '.html')
        return func
    return _page

@page('index')
def index():
    return {'title': 'Home'}

@page('gallery')
def gallery():
    entries = yaml.load(open("gallery.yaml", "r"))
    return {'entries': entries}

@page('development')
def development():
    return {}

@page('community')
def community():
    return {}

@page('members')
def members():
    members = yaml.load(open("members.yaml", "r"))
    members.sort(key = lambda a: a['name'].split()[-1])
    return {'members': members}

@page('about')
def about():
    return {}

def main():
    for name in sorted(pages):
        setup_func, template_name = pages[name]
        out_name = os.path.join("output", template_name)
        context = {'theme': 'cyborg', 'title': name}
        context.update(setup_func())
        with open(out_name, "w") as f:
            html = render_template(template_name, context)
            f.write(html)

if __name__ == "__main__":
    main()
