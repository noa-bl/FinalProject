FROM  python:alpine
WORKDIR /app
COPY ./Application/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install --no-cache-dir -r requirements.txt
COPY ./Application .
EXPOSE 5555
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
CMD ["flask", "run"]