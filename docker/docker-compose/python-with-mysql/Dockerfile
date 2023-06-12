FROM python:3
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py", "--user", "root"]