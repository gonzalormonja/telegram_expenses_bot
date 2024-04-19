import { SupabaseClient, createClient } from "@supabase/supabase-js";
import { Database } from "database.types";
import { env } from "process";

export class UserRepository {
    private supabase: SupabaseClient<Database>
    constructor() {
        this.supabase = createClient<Database>(env.SUPABASE_URL, env.SUPABASE_KEY)
    }

    public async getByTelegramId(telegramId: string) {
        const resp = await this.supabase.from('users').select('*').eq('telegram_id', telegramId).single()
        return resp ? resp.data : null
    }
}