FROM docker.io/library/python:3.9

WORKDIR ~

RUN mkdir saulo-project0
RUN chdir saulo-project0

COPY requirements.txt .
RUN python3 -m venv venv

RUN venv/bin/python3 -m pip install -r requirements.txt

COPY . .

CMD ["venv/bin/python3", "-m", "main.py" "-h"]
