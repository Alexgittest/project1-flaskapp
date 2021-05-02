FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
COPY birthday.txt ./
ENV AWS_ACCESS_KEY_ID=AKIAQ535QKIOYKBFNXYS
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_DEFAULT_REGION=us-east-1
CMD [ "python", "./app.py" ]
