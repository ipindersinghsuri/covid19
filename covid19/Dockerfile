FROM python:3.8

ADD requirements.txt .

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt --ignore-installed --no-input

RUN mkdir -p /code/covid19
COPY . /code/covid19

CMD ["uwsgi", "--ini", "/code/covid19/uwsgi.ini"]