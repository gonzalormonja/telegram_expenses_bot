import { UserRepository } from "./user.repository.js";
import jwt from 'jsonwebtoken'

export class UserService {
    private userRepository: UserRepository
    constructor() {
        this.userRepository = new UserRepository()
    }

    public async getByTelegramId(telegramId: string) {
        return this.userRepository.getByTelegramId(telegramId)
    }

    public async getUserToken(user: User): Promise<string> {
        return jwt.sign(user, process.env.JWT_SECRET, { expiresIn: '10m' })
    }
}

interface User {
    id: number;
    telegram_id: string;
}