# Containeriser une application Python Flask et sa database persistante avec Docker

Mini-projet dans le cadre de la formation Administration système DevOps de M2i Formations.  
Fait sous Debian 12

## Process
1. Cloner le projet
```bash
git clone https://github.com/oyokai/reunions.git
```
2. Créer un environnement virtuel et vérifier que l'application fonctionne
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```
3. Si nécessaire, installer Docker from scratch
```bash
sudo apt remove docker docker-engine docker.io containerd runc
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release

sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release && echo "$ID")/gpg \
  | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://download.docker.com/linux/$(. /etc/os-release && echo "$ID") \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

docker --version
sudo systemctl status docker
docker compose version
```
4. Créer les fichiers Dockerfile, docker-compose.yml (fournis dans le repo)
5. Créer les scripts create_db.py et wait_db.py (fournis dans le repo)
6. Remplacer config.py avec celui du repo
7. Installer la dépendance cryptography
```bash
pip install cryptography
pip freeze > requirements.txt
```
8. Lancer
```bash
sudo docker compose up -d -build
```
