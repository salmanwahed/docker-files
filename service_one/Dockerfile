FROM python:3.8-alpine
WORKDIR /todoapp
COPY requirements.txt .
RUN pip install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]

