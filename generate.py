from __future__ import print_function
import git
import yaml
import os
import sys
import tempfile
from jinja2 import Environment, FileSystemLoader

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

try:
    yt_path = str(importlib_resources.files("yt"))
except ModuleNotFoundError:
    yt_path = None
else:
    if not (yt_path / '.git').is_dir():
        yt_path = None

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

pages = {}

def page(name, output_name = None):
    if output_name is None:
        output_name = name + '.html'
    def _page(func):
        pages[name] = (func, output_name)
        return func
    return _page

@page('index')
def index():
    examples = yaml.load(open("examples.yaml", "r"), Loader=yaml.SafeLoader)
    return {'title': 'Home', 'examples': examples}

@page('gallery')
def gallery():
    entries = yaml.load(open("gallery.yaml", "r"), Loader=yaml.SafeLoader)
    return {'entries': entries}

name_ignores = ["convert-repo"]

def lastname_sort(a):
    return a.rsplit(None, 1)[-1]

@page('about')
def about():
    # Uncomment for rapid dev
    if "--fast" in sys.argv:
        return {'developers': []}
    if yt_path:
        repo = git.Repo(yt_path)
    else:
        with tempfile.TemporaryDirectory() as repo_path:
            with git.Repo.clone_from(
                "https://github.com/yt-project/yt", repo_path
            ) as repo:
                shortlog = repo.git.shortlog(["-ns", "HEAD"]).split("\n")
    devs = set([sl.split("\t")[1] for sl in shortlog])
    for name in name_ignores:
        devs.discard(name)
    return {"developers": sorted(devs, key=lastname_sort)}

@page('community')
def community():
    return {}

@page('members')
def members():
    members = yaml.load(open("members.yaml", "r"), Loader=yaml.SafeLoader)
    members.sort(key = lambda a: lastname_sort(a['name']))
    return {'members': members}

@page('development')
def development():
    return {}

@page('data/index')
def data():
    return {'url_prefix':'../'}

@page('workshops/spring2019/index')
def data():
    return {'url_prefix':'../../'}

@page('extensions')
def extensions():
    extensions = yaml.load(open("extensions.yaml", "r"), Loader=yaml.SafeLoader)
    return {'extensions': extensions}

@page('slack')
def slack():
    return {}

def main():
    for name in sorted(pages):
        setup_func, template_name = pages[name]
        out_name = os.path.join(".", template_name)
        dir_name = os.path.dirname(out_name)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        context = {'theme': 'flatly', 'title': name,
                   'url_prefix': ''}
        context.update(setup_func())
        with open(out_name, "w") as f:
            html = render_template(template_name, context)
            if sys.version_info.major < 3:
                html = html.encode('utf8')
            f.write(html)

if __name__ == "__main__":
    main()
