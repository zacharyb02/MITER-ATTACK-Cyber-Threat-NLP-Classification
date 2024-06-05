FROM tiangolo/uvicorn-gunicorn:python3.10

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app