FROM python:3.12.2-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Copy supervisord.conf file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8000

CMD ["/usr/bin/supervisord"]
