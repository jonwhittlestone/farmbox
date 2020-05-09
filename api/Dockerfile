# pull official base image
FROM nickgryg/alpine-pandas

# set work directory
WORKDIR /usr/src/app
RUN apk update
RUN apk add make automake libressl-dev libffi-dev gcc g++ python3-dev subversion libxml2-dev libxslt-dev curl
RUN pip3 install --upgrade pip
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
