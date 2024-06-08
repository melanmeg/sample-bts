FROM python:3.12.3-alpine3.20

WORKDIR /api-server
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV DATABASE_URL=driver://user:pass@localhost/dbname

COPY . .
RUN chmod +x ./entrypoint.sh

HEALTHCHECK --interval=1s --timeout=3s --start-period=1s --retries=5 \
  CMD wget -q -O - http://api-server:8000 || exit 1

ENTRYPOINT [ "./entrypoint.sh" ]