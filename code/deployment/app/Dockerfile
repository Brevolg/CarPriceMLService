FROM python:3.11


WORKDIR /app


COPY code/deployment/app/requirements.txt .


RUN pip install -r requirements.txt


COPY code/deployment/app/app.py .


CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]