FROM python:latest

RUN mkdir -p ~/BSUIR/ISP/docker/
WORKDIR ~/BSUIR/ISP/docker
ADD ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
ADD . .

CMD ["python3","ramanujan.py"]
