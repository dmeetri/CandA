FROM python:3.14-slim

WORKDIR /app

COPY CN/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY CN/ /app/

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "CN.wsgi:application"]