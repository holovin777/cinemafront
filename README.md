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
