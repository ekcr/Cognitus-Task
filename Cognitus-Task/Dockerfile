FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
RUN pip install --upgrade pip

# RUN pip install fastapi uvicorn
COPY  requirements.txt requirements.txt
RUN  pip install -r requirements.txt
RUN pip install scikit-learn
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install psycopg2


# EXPOSE 80

COPY . /app

# CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","80" ]