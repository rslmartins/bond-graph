#Install Python/Debian OS
FROM python:3.7

#Set working directory as /app
WORKDIR /app

#Copy the content into /app
COPY . /app

#Install the requirements for OS and Python
RUN chmod +x ./requirements.sh
RUN ./requirements.sh

#Set streamlit app as default
CMD streamlit run --server.port $PORT app.py
