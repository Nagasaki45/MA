*Tom Gurion research proposal, Bar-Ilan University*

# Audio-Only Augmented Reality System for Social Interaction

### Some notes about the tags

- *v1.0*: First research proposal submitted (February 2013). Not part of this repo.
- *v2.0*: Second research proposal submitted (March 2014).
- *v3.0*: Thesis. Work in progress...

### Source compilation

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