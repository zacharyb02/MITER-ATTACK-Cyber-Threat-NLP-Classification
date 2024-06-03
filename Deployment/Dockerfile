FROM python:3.10.11
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV PORT 80  
EXPOSE $PORT  
CMD exec gunicorn -w 4 -b 0.0.0.0:$PORT wsgi:app
