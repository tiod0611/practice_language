FROM python:3
COPY . /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt
CMD ["python", "main.py", "--user", "root"]