import os
from expense.expense_repository import ExpenseRepository
from langchain_openai import OpenAI


class ExpenseService:
    """
    Class for managing expense services.
    """

    def __init__(self):
        self.expense_repository = ExpenseRepository()

    def __process_message(self, text: str) -> dict:
        """
        Get category and amount from langchain_openai and return {"category": str, "amount": float}
        """
        llm = OpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))

        question = f'Hello, you are a sentence sorter and you must sort the sentence I am about to tell you into one of these expense categories. Please answer a word that represents exactly one of the words in the following matrix(Do not translate the category please) then, separated by "," put the amount(just the number).if you think the message is not an expense, for example it is a greeting or you cant find the complete information for example the amount is missing(buy pizza for example) answer None. If you contact a purchase but you cant find it in a category and we have a category for others, use it. {os.environ.get("CATEGORIES")}  Phrase is:  "{text}"'

        answer = llm.predict(question).strip()

        if answer == 'None' or len(answer.split(',')) != 2:
            raise Exception('The message is not an expense')

        return {
            'amount': float(answer.split(',')[1]),
            'category': answer.split(',')[0]
        }

    def save_expense(self,
                     user_id: str,
                     text: str) -> dict:
        """
        Get category and amount from text, save expense and return {"category": str, "amount": float}
        """
        process_message = self.__process_message(text)

        self.expense_repository.create(
            user_id, text, process_message['amount'], process_message['category'])

        return process_message
