import { Client } from 'pg'

export class UserRepository {
    constructor(private db: Client) { }

    public async create(telegram_id: string) {
        const query = 'INSERT INTO users (telegram_id) VALUES ($1) RETURNING *'
        const values = [telegram_id]
        const resp = await this.db.query(query, values)
        return resp.rows[0]
    }

    public async getByTelegramId(telegramId: string) {
        const query = 'SELECT * FROM users WHERE telegram_id = $1'
        const values = [telegramId]
        const resp = await this.db.query(query, values)
        return resp.rows[0]
    }
}