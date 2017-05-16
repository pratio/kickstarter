FROM python:2.7

## Python script to download google analytics data
ADD kickstarter_django /usr/src/kickstarter_django

## Install the requirements
RUN pip install --upgrade pip
RUN cd /usr/src/kickstarter_django && \
while read in; do pip install "$in"; done < requirements.txt

## Change timezone
RUN echo "Europe/Berlin" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
