FROM python:3.10

RUN pip install gradio

COPY app.py app.py

EXPOSE 8080

CMD ["python", "app.py"]