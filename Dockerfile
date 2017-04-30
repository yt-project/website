FROM continuumio/miniconda

COPY . /srv/website
RUN conda install -qy jinja2 git
RUN pip install gitpython
WORKDIR /srv/website
RUN python generate.py

EXPOSE 80
CMD ["python", "-m", "SimpleHTTPServer", "80"]
