FROM python:3.7.1-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
ENV NAME houdongdong
CMD ["python", "application.py"]