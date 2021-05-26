FROM python:2.7.15
MAINTAINER RobertLC
LABEL description="pysatools_heroku_build"

# Install required system packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	python3  \
	python3-pip && \
    apt-get clean

ADD razorz /home/razorz/

COPY requirements.txt /var/
RUN rm -rf /etc/hosts
COPY hosts.txt /etc/hosts

RUN pip install --no-cache-dir -r /var/requirements.txt 
RUN pip3 install --no-cache-dir -r /var/requirements.txt 
RUN pip install PySocks
RUN pip3 install PySocks

RUN wget http://www.halacima.net
RUN wget http://www.cimalina.com

ADD run.py /home/run.py

CMD python3 /home/run.py "$THE_URL" -w "$THE_WORKER" -s "$THE_STATUS"
