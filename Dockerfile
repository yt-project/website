FROM continuumio/miniconda

COPY . /srv/website
RUN conda install -qy jinja2 mercurial
RUN pip install python-hglib
WORKDIR /srv/website
RUN python generate.py

EXPOSE 80
CMD ["python", "-m", "SimpleHTTPServer", "80"]
