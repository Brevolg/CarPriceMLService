## Run pipeline

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run the complete pipeline:

``` bash
dvc repro
```

## Access services

After successful pipeline execution:

FastAPI API documentation:

    http://localhost:8000/docs

Streamlit web application:

    http://localhost:8501

## Automatic execution

The pipeline is automatically executed every 5 minutes using Windows
Task Scheduler.

The scheduler runs:

    dvc repro

which executes all pipeline stages.
