FROM python:3

WORKDIR /opt

## Seperate copy actions to prevent image bloat from pip installs
COPY term21-webui/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD term21-webui /opt/term21-webui


EXPOSE 8080

CMD [ "python", "-m", "term21-webui.wsgi" ]