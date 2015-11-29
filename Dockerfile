FROM hiono/texlive

ENV LANG=en_US.UTF-8
RUN apt-get update -y
RUN apt-get install -y git
RUN apt-get install -y inkscape

COPY . /thesis
RUN git clone https://github.com/Nagasaki45/MA-experiment-analysis.git
WORKDIR /thesis

CMD python3 manage.py all
