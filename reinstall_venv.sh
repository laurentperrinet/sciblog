#!/bin/zsh
# Réinstaller tous les paquets dans le .venv Python 3.13
cd "$(dirname "$0")"

pip install --upgrade pip

pip install \
  nikola \
  jupyterlab \
  ipykernel \
  numpy \
  scipy \
  matplotlib \
  pillow \
  requests \
  lxml \
  mako \
  markdown \
  ghp-import \
  doit \
  natsort \
  Unidecode \
  MotionClouds \
  watermark \
  imageio \
  rst2html5 \
  PyRSS2Gen \
  Genshi \
  pyzmq \
  psutil \
  cloudpickle \
  piexif \
  webencodings \
  websocket-client \
  types-python-dateutil

# Enregistrer le noyau Jupyter pour VS Code
python -m ipykernel install --user --name sciblog --display-name "Python (sciblog)"

echo ""
echo "✓ Installation terminée"
echo "✓ Noyau 'Python (sciblog)' enregistré"
echo ""
echo "→ Rechargez VS Code : Cmd+Shift+P > 'Developer: Reload Window'"
