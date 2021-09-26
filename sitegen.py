import os
from jinja2 import Environment, FileSystemLoader
import urllib.request, json

if not os.path.isdir(".www"):
    os.mkdir(".www")
    api_url = input("Your API url: ")
    site_name = input("Your site name: ")
    site_conf = { "site_name": site_name, "api_url": api_url }
    with open(".www/conf.json", "w") as conf_file:
        json.dump(site_conf, conf_file)

with open(".www/conf.json", "r") as conf_file:
    site_conf = json.load(conf_file)

    with urllib.request.urlopen(site_conf["api_url"]) as url:
        data = json.loads(url.read().decode())
        articles_api = []
        i = 0
        while i < len(data):
            articles_api.append(data[i])
            i += 1
        env = Environment(loader = FileSystemLoader("./"))
        template = env.get_template("jinja2.html")
        styles = env.get_template("jinja2styles.css")
        index_output = open(".www/index.html", "w")
        index_output.write(template.render(site_name = site_conf["site_name"], articles = articles_api))
        styles_output = open(".www/styles.css", "w")
        styles_output.write(styles.render( articles = articles_api))
