import axios from "axios";
import { env } from "process";
import { Telegraf } from "telegraf";
import { message } from 'telegraf/filters'
import { UserService } from "./../user/user.service.js";
import { Client } from "pg";

export class TelegramHandlerController {

    private bot: Telegraf
    private userService: UserService

    constructor(private db: Client) {
        const token = env.TELEGRAM_BOT_TOKEN;
        this.bot = new Telegraf(token);
        this.userService = new UserService(this.db)
    }

    public async listen() {
        this.bot.on(message('text'), async (ctx) => {
            try {

                const user = await this.userService.getByTelegramId(ctx.message.chat.id.toString());
                if (!user) {
                    return
                }
                const userToken = await this.userService.getUserToken(user)

                const response = await axios.post(
                    `${env.CLASSIFICATION_API_URL}/api/v1/expense`,
                    {
                        text: ctx.message.text,
                        telegram_id: ctx.message.chat.id,
                    },
                    {
                        headers: {
                            'Authorization': `Bearer ${userToken}`
                        }
                    }
                );

                if (response.data.message) {
                    ctx.reply(response.data.message);
                }
            } catch (e) {
                if (e['response'] && e['response']['status'] === 401) {
                    return
                }
                ctx.reply('Something went wrong!');
            }
        });
        await this.bot.launch();
    }
}