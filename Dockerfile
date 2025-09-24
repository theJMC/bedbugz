FROM node:22 as builder

WORKDIR /app

COPY bedbugz/package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci
COPY bedbugz ./
RUN --mount=type=cache,target=/root/.npm npm run build

FROM node:22 as runner
WORKDIR /app
COPY --from=builder /app/.output/server ./server
COPY --from=builder /app/.output/public ./public

EXPOSE 3000
CMD ["node", "/app/server/index.mjs"]