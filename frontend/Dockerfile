# base image
FROM node:lts-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install --silent
COPY . .

# start app
CMD ["npm", "run", "serve"]