# Etape pour lancer l'application

## 1 - Installer python sur la machine

## 2 - Creer une environnement virtuelle python 
```bash
# Windows
python -m venv venv

#linux
python3 -m venv venv
```

## 3 - Acceder a cette environnement virtuelle
```bash
#Windows
.\venv\Scripts\Activate # ou activate 

#linux
source venv/bin/activate 
```

## 4 - Installer les dependances
```bash
pip install -r requirements.txt
```

## 5 - Lancer l'application 
```bash
python run.p
```