ARG ALPINE_VERSION=3.21
ARG PYTHON_VERSION=3.13.2

FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

WORKDIR /api-server
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x ./entrypoint.sh

HEALTHCHECK --interval=30s --timeout=3s --start-period=1s --retries=5 \
  CMD wget -q -O - http://api-server:8000 || exit 1

ENTRYPOINT [ "./entrypoint.sh" ]
