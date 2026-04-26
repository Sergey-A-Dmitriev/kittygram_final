FROM node:18
WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm ci

COPY . .
RUN npm run build
# RUN npm install --global http-server

FROM alpine:latest
COPY --from=builder /app/build /static
# CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]
