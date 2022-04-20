FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install Flask==2.0.3 \
                 redis                                  

COPY app.py /data/app.py
COPY ML_Data_Sample.json /data/ML_Data_Sample.json

WORKDIR /data/

CMD ["python3", "/data/app.py"]

