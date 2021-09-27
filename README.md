# sitegen
Python site generator for api json

## Pre-install for ArchLinux
```bash
sudo pacman -S caddy
```
## Installation guide
```bash
git clone https://github.com/holovin777/sitegen.git
cd sitegen
```
Create new repository `www`.
```bash
git clone git@github.com:<your_user>/www.git
```
```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python sitegen.py
cd www
caddy file-server --listen :3000
```
