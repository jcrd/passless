FROM supplantr/iniq-testrunner

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install lesspass
