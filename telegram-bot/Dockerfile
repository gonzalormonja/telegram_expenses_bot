from node:18.12.1

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

CMD ["npx", "ts-node", "src/index.ts"]