FROM biansepang/weebproject:buster

# Dockerfile
# KING
# Dockerfile
RUN git clone -b King-Userbot https://github.com/AftahBagas/Alpha_ /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/AftahBagas/Alpha_/Alpha/requirements.txt

CMD ["python3","-m","userbot"]
