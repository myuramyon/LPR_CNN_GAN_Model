FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "src/main.py", "--input", "/data/cctv.mp4", "--output", "/data/out.mp4"]
