FROM python:3.6

ENV PYTHONBUFFERED 1
RUN mkdir /backend
WORKDIR /backend

COPY ./requirements.txt /backend

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt

COPY . /backend/

ENTRYPOINT ["/backend/entrypoint.sh"]
