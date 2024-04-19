import { Request, Response } from "express";
import { UserService } from "./user.service.js"
import { Client } from "pg";

export class UserController {
    private userService: UserService

    constructor(private db: Client) {
        this.userService = new UserService(this.db)
    }

    public async create(req: Request, res: Response) {
        try {
            const telegram_id = 'telegram_id' in req.body ? req.body.telegram_id : null
            if (!telegram_id) {
                throw new Error('telegram_id is required')
            }
            const user = await this.userService.create(telegram_id)
            res.status(201).json(user)
        } catch (error) {
            res.status(400).json({ error: error.message })
        }
    }
}