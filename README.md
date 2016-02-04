*Tom Gurion research proposal, Bar-Ilan University*

# An Audio-Only Augmented Reality System for Social Interaction

### Some notes about the tags

- *v1.0*: First research proposal submitted (February 2013). Not part of this repo.
- *v2.0*: Second research proposal submitted (March 2014).
- *v3.0*: Thesis first submission (August 23, 2015).
- *v3.1*: Several minor fixes. 3 printed copies @ the Music Department library (November, 2015).
- *v3.2*: Last thesis submission after formal typesetting improvements (January, 2016).

### Source compilation

The ``manage.py`` script is your friend for simple compilation of the source.

Options are: clear, graphics, plots, pdf & all.

Each of those can be used to build different stages of the final pdf.

Currently, all of the plots reside in external git repo and copied by demand.
This repo can be found [here](https://github.com/Nagasaki45/MA-experiment-analysis).
Clone this repo and fix the path to it in ``manage.py`` as needed.

### Compiling with docker

The following will run ``python manage.py all`` in a docker container:

	docker build -t ma .
	docker run ma

To copy the pdf file out of the container find the container ID using ``docker ps --all`` and run:

	docker cp <ID>:/thesis/thesis_<SHORT_COMMIT_HASH>.pdf .
