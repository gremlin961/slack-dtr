FROM python:2.7-alpine
ENV slack_url "enter_your_Slack_API_URL_here"
#RUN pip install flask requests jinja2 tinydb
RUN mkdir /database
#ADD app.py /app.py
COPY ./ /
RUN pip install -r requirements.txt
ENV FLASK_APP /run.py
CMD python -m flask run --host=0.0.0.0 --port=8080
