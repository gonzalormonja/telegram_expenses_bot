from datetime import datetime, timezone
import os
import psycopg2


class ExpenseRepository:
    """
    Class for the repository of the expense.
    """

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DBNAME"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT"),
        )

    def create(self,
               user_id: str,
               description: str,
               amount: float,
               category: str) -> bool:
        """
        Create new expense in the database.
        """
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO expenses (user_id, description, amount, category, added_at) VALUES (%s, %s, %s, %s, %s)",
            (user_id, description, amount, category,
             datetime.now().astimezone(timezone.utc))
        )
        self.conn.commit()
        cur.close()
