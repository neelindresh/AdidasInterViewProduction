FROM python:3.8-buster

# Create app directory
WORKDIR /production

# Install app dependencies
COPY requirement.txt ./

RUN pip install -r requirement.txt

# Bundle app source
COPY app/ .

EXPOSE 5005
CMD [ "python", "app.py","--host","0.0.0.0","-p","5005"]