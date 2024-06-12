FROM node:22.2.0-alpine3.20

WORKDIR /web-server
COPY ./app/package.json ./app/package-lock.json ./
RUN npm install

COPY ./app .

ENTRYPOINT [ "npm", "start" ]