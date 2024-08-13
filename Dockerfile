FROM python:3.12.5-alpine

WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN printf '[default]\nSECRET_KEY="DEMO_KEY"' > config/.secrets.toml 

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
