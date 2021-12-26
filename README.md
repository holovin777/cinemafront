# cinemafront
Python site generator for api json

## Pre-install for ArchLinux
```bash
sudo pacman -S caddy
```
## Installation guide
```bash
git clone https://github.com/holovin777/cinemafront.git
cd cinemafront
```
Create new repository `cinemawww`.
```bash
git clone git@github.com:<your_user>/cinemawww.git
```
```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python cinemafront.py
cd cinemawww
caddy file-server --listen :3000
```
