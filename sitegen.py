import os
import subprocess
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
if not os.path.isdir(".www"):
    os.mkdir(".www")
index = open(".www/index.html", "w")
index.write(template.render(site_name = site_name_input, articles = articles_api))
subprocess.run(["cp", "styles.css", ".www/styles.css"])
