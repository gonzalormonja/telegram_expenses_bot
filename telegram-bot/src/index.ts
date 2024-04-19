import * as dotenv from 'dotenv';
import { TelegramHandlerController } from './telegram-handler/telegram-handler.controller.js';
import express from 'express'
import bodyParser from 'body-parser'
import { UserController } from './user/user.controller.js';
import pkg from 'pg';
const { Client } = pkg
import { env } from 'process';

dotenv.config();

const app = express();
const port = 3000;



async function main() {
	const db = new Client(env.POSTGRES_URL)
	db.connect().then(() => {
		const telegramHandlerController = new TelegramHandlerController(db)
		const userController = new UserController(db)
		app.use(bodyParser.json());

		app.post('/api/v1/users', (req, res) => userController.create(req, res))

		app.listen(port, async () => {
			console.log(`Server start at http://localhost:${port}`);
			await telegramHandlerController.listen()
		});
	})

}

main()