FROM python:3.12-alpine
RUN pip3 install Flask
WORKDIR /app
COPY app/* /app
CMD ["python3", "app.py"]
