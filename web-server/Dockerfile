FROM node:22.2.0-alpine3.20

WORKDIR /web-server
COPY ./app/package.json ./app/package-lock.json ./
RUN npm install

COPY ./app .

HEALTHCHECK --interval=1s --timeout=3s --start-period=1s --retries=5 \
  CMD wget -q -O - http://web-server:3000 || exit 1

ENTRYPOINT [ "npm", "start" ]