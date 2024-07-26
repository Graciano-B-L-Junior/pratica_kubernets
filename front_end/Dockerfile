FROM node:22-bookworm-slim

WORKDIR /app

COPY . /app

RUN npm i

EXPOSE 3001

CMD [ "node", "server.js" ]