from datetime import datetime, timezone
import os
from supabase import create_client, Client


class ExpenseRepository:
    """
    Class for the repository of the expense.
    """

    db = None

    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def create(self,
               user_id: str,
               description: str,
               amount: float,
               category: str) -> bool:
        """
        Create new expense in the database.
        """
        self.supabase.table('expenses').insert({
            "user_id": user_id,
            "description": description,
            "amount": amount,
            "category": category,
            "added_at": datetime.now().astimezone(timezone.utc).isoformat()
        }).execute()
