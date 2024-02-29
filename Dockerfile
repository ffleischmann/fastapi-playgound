FROM python:3.11 as base

COPY ./requirements.txt /requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

FROM base as main_api

WORKDIR /app

EXPOSE 8000

CMD ["python3.11", "-m", "uvicorn", "main:app", "--host", "0.0.0.0",  "--port", "8000", "--reload"]

FROM base as dummy_api

WORKDIR /dummy-api

EXPOSE 8001

CMD ["python3.11", "-m", "uvicorn", "main:app", "--workers", "8", "--host", "0.0.0.0", "--port", "8001"]