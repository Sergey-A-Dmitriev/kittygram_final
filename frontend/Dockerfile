FROM node:18 AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
FROM alpine:latest
RUN adduser -D -u 1000 static
RUN mkdir -p /static && chown -R static:static /static
COPY --from=builder --chown=static:static /app/build /static
VOLUME ["/static"]
USER static
CMD ["sh", "-c", "echo 'Static volume is ready' && sleep infinity"]