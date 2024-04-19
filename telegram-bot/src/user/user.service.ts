import jwt from 'jsonwebtoken';
import { Client } from 'pg';
import { UserRepository } from './user.repository.js';

export class UserService {
	private userRepository: UserRepository;
	constructor(private db: Client) {
		this.userRepository = new UserRepository(this.db);
	}

	public async create(telegram_id) {
		const user = await this.getByTelegramId(telegram_id);
		if (user) {
			throw new Error('User already exist');
		}
		return this.userRepository.create(telegram_id);
	}

	public async getByTelegramId(telegramId: string) {
		return this.userRepository.getByTelegramId(telegramId);
	}

	public async getUserToken(user: User): Promise<string> {
		return jwt.sign(user, process.env.JWT_SECRET, { expiresIn: '10m' });
	}
}

interface User {
	id: number;
	telegram_id: string;
}
