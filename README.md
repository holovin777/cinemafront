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
python sitegen.py
cd .www
caddy file-server --listen :3000
```
## Deploy with GitHub
Create a new public repository
Quick setup with SSH
```bash
cd .www
git init
git add .
git commit -m "First push"
git branch -M main
git remote add origin git@github.com:<your_user>/<your_repository>.git
git push -u origin main
```
Enter in your repository Settings/Pages. For Source select main branch and save.
