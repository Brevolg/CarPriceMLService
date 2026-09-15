FROM python:3.11


WORKDIR /app


COPY code/deployment/api/requirements.txt .


RUN pip install -r requirements.txt


COPY code/deployment/api/main.py .


COPY models/model.pkl .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]