ARG ALPINE_VERSION=3.21
ARG NODE_VERSION=23.10.0
ARG NGINX_VERSION=1.27.4

FROM node:${NODE_VERSION}-alpine${ALPINE_VERSION} AS build

WORKDIR /frontend
COPY ./frontend .

RUN npm i
RUN npm run build

FROM nginx:${NGINX_VERSION}-alpine${ALPINE_VERSION}

WORKDIR /usr/share/nginx/html
COPY --from=build /frontend/build /usr/share/nginx/html

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

HEALTHCHECK --interval=30s --timeout=3s --start-period=1s --retries=5 \
  CMD wget -q -O - http://web-server/health || exit 1
