FROM python:3.7
EXPOSE 5000
COPY ./app /app
COPY ./requirements.txt requirements.txt 
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]