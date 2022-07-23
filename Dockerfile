FROM python:3.9.13

WORKDIR /trmanh29_hackathon
COPY . /trmanh29_hackathon

# ENV GOOGLE_APPLICATION_CREDENTIALS=secret.json
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh
CMD ./run.sh