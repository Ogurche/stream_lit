FROM python:latest

WORKDIR /app

VOLUME [ "/app" ]

COPY requirement.txt ./requirement.txt

RUN pip3 install -r requirement.txt

COPY db.py .

COPY main.py .

COPY test.db .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]