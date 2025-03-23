ARG ALPINE_VERSION=3.21
ARG POSTGRES_VERSION=15.12

FROM postgres:${POSTGRES_VERSION}-alpine${ALPINE_VERSION}

COPY ./postgresql.conf /etc/postgresql/postgresql.conf
COPY ./pg_hba.conf /etc/postgresql/pg_hba.conf

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
