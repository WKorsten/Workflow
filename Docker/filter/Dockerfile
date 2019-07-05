FROM python:3.6

EXPOSE 5000

WORKDIR /filter

COPY requirements.txt /filter

RUN pip install -r requirements.txt


COPY filter.py /filter
CMD python filter.py
