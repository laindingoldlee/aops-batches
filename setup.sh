#!/bin/bash
# One-time environment setup for a fresh cloud session (Ubuntu). Safe to re-run.
# Installs Asymptote, pdflatex (+ asymptote.sty) and the Python packages the tools need.
set -e
SUDO=""; [ "$(id -u)" != "0" ] && SUDO="sudo"
need=""
command -v asy >/dev/null || need="$need asymptote"
command -v pdflatex >/dev/null || need="$need texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended"
kpsewhich asymptote.sty >/dev/null 2>&1 || need="$need asymptote texlive-latex-extra"
if [ -n "$need" ]; then
  export DEBIAN_FRONTEND=noninteractive
  $SUDO apt-get update -qq
  $SUDO apt-get install -y -qq --no-install-recommends $need ghostscript dvisvgm libcairo2 >/dev/null
fi
python3 -c "import cairosvg, PIL, sympy, numpy" 2>/dev/null || pip install -q cairosvg pillow sympy numpy 2>/dev/null || pip install -q --break-system-packages cairosvg pillow sympy numpy
echo "asy: $(asy -version 2>&1 | head -1)"
echo "pdflatex: $(pdflatex -version | head -1)"
kpsewhich asymptote.sty
python3 -c "import cairosvg, PIL, sympy, numpy; print('python packages OK')"
# smoke test: one Asymptote figure to SVG
d=$(mktemp -d); printf 'settings.outformat="svg";\nsettings.render=0;\nsize(3cm);draw(unitcircle);label("$A$",(1,0),E);\n' > $d/t.asy
(cd $d && asy -f svg t.asy) && [ -s $d/t.svg ] && echo "SETUP OK" || { echo "asy smoke test FAILED"; exit 1; }
