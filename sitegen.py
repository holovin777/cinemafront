import os
from jinja2 import Environment, FileSystemLoader
import urllib.request, json

articles_api = []
api_url = input("Your API url: ")

with urllib.request.urlopen(api_url) as url:
    data = json.loads(url.read().decode())
    i = 0
    while i < len(data):
        articles_api.append(data[i])
        i += 1

site_name_input = input("Your site name: ")
env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("jinja2.html")
styles = env.get_template("jinja2styles.css")
if not os.path.isdir(".www"):
    os.mkdir(".www")
index_output = open(".www/index.html", "w")
index_output.write(template.render(site_name = site_name_input, articles = articles_api))
styles_output = open(".www/styles.css", "w")
styles_output.write(styles.render( articles = articles_api))
