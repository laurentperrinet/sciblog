git clone git://github.com/getnikola/nikola.git
cd nikola
pip install -r requirements-full.txt
pip install .
nikola init --demo invibe
nikola build
nikola serve

