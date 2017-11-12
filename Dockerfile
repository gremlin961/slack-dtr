FROM python:2.7-alpine
ENV slack_url "enter_your_Slack_API_URL_here"
RUN pip install flask requests
ADD app.py /app.py
ENV FLASK_APP /app.py
CMD python -m flask run --host=0.0.0.0 --port=8080
