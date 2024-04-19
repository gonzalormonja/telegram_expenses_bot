import * as dotenv from 'dotenv';
import { TelegramHandlerController } from './telegram-handler/telegram-handler.controller.js';

dotenv.config();

async function main() {
	const telegramHandlerController = new TelegramHandlerController()
	await telegramHandlerController.listen()
}

main()