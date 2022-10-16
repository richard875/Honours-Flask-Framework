FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask

WORKDIR /flask-app

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# Build: docker build -t flask-experiment .
# Run: docker run -p 5500:5000 flask-experiment