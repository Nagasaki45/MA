### Tom Gurion research proposal, Bar-Ilan University

# Audio-Only Augmented Reality System for Social Interaction

In order to compile the LaTeX be sure that the SVGs are already compiled
using Inkscape.

```bash
cd graphics
inkscape -D -z --file=<FILENAME>.svg --export-pdf=<FILENAME>.pdf --export-latex  # for every SVG file
```

Then you are ready to compile the document itself.

```bash
pdflatex research_proposal.tex
biber research_proposal.bcf
pdflatex research_proposal.tex
pdflatex research_proposal.tex
```

In order to clear the directory from unnecessary TeX files run:

```bash
python clear.py
```