from __future__ import print_function
import yaml
import os
from jinja2 import Environment, FileSystemLoader
import hglib
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

import pkg_resources
yt_provider = pkg_resources.get_provider("yt")
yt_path = os.path.dirname(yt_provider.module_path)

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
    return {'title': 'Home'}

@page('gallery')
def gallery():
    entries = yaml.load(open("gallery.yaml", "r"))
    return {'entries': entries}

name_mappings = {
        # Sometimes things get filtered out by hgchurn pointing elsewhere.
        # So we can add them back in manually
        "andrew.wetzel@yale.edu" : "Andrew Wetzel",
        "df11c@my.fsu.edu": "Daniel Fenn",
        "dnarayan@haverford.edu": "Desika Narayanan",
        "jmtomlinson95@gmail.com": "Joseph Tomlinson",
        "kaylea.nelson@yale.edu": "Kaylea Nelson",
        "tabel@slac.stanford.edu": "Tom Abel",
        "pshriwise": "Patrick Shriwise",
        "jnaiman": "Jill Naiman",
        "gsiisg": "Geoffrey So",
        "dcollins4096@gmail.com": "David Collins",
        "bcrosby": "Brian Crosby",
        "astrugarek": "Antoine Strugarek",
        "AJ": "Allyson Julian",
}

name_ignores = ["convert-repo"]

lastname_sort = lambda a: a.rsplit(None, 1)[-1]

@page('about')
def about():
    import hglib
    from email.utils import parseaddr
    cmd = hglib.util.cmdbuilder("churn", "-c")
    c = hglib.open(yt_path)
    emails = set([])
    for dev in c.rawcommand(cmd).split("\n"):
        if len(dev.strip()) == 0: continue
        emails.add(dev.rsplit(None, 2)[0])
    print("Generating real names for {0} emails".format(len(emails)))
    names = set([])
    for email in sorted(emails):
        if email in name_ignores:
            continue
        if email in name_mappings:
            names.add(name_mappings[email])
            continue
        cset = c.log(revrange="last(author('%s'))" % email)
        if len(cset) == 0:
            print("Error finding {0}".format(email))
            realname = email
        else:
            realname, addr = parseaddr(cset[0][4])
        if realname == '':
            realname = email
        if realname in name_mappings:
            names.add(name_mappings[realname])
            continue
        realname = realname.decode('utf-8')
        realname = realname.encode('ascii', 'xmlcharrefreplace')
        names.add(realname)
    devs = list(names)
    devs.sort(key=lastname_sort)
    return {'developers': devs}

@page('community')
def community():
    return {}

@page('members')
def members():
    members = yaml.load(open("members.yaml", "r"))
    members.sort(key = lambda a: lastname_sort(a['name']))
    return {'members': members}

@page('development')
def development():
    return {}

@page('data/index')
def data():
    return {'url_prefix':'../'}

def main():
    for name in sorted(pages):
        setup_func, template_name = pages[name]
        out_name = os.path.join(".", template_name)
        context = {'theme': 'flatly', 'title': name,
                   'url_prefix': ''}
        context.update(setup_func())
        with open(out_name, "w") as f:
            html = render_template(template_name, context)
            f.write(html)

if __name__ == "__main__":
    main()
