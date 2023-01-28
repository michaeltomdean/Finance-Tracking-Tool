import sqlite3
from datetime import datetime
from misc.tools import get_user_data_path


class FinanceSQL:
    def __init__(self):
        self.path = fr"{get_user_data_path()}/finance.db"
        self.connection, self.cursor = self.connect()

    def connect(self):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        return connection, cursor

    def get_all_spending(self):
        self.cursor.execute("""
        SELECT * FROM spending
        """)
        return self.cursor.fetchall()

    def add_spending_record(self, name: str, category: str, date: str, amount: float, typ: str):
        """
        Adds transactions to finance database
        :param name: Name of the transaction. Ex Tesco, Apple etc.
        :param category: Category from list of categories list.
        :param date: Date when the transaction was made YYYY-MM-DD.
        :param amount: amount of transaction.
        :param typ: Type of transaction. Is it a need? (N) want? (W) save? (S)
        :return:
        """
        sql_insert_query = (
            """
            INSERT INTO spending
            (name, category, datetime, amount, type)
            VALUES (?,?,?,?,?)
            """
        )
        self.cursor.execute(sql_insert_query, (name, category, date, amount, typ))
        self.connection.commit()

    def get_last_monthly_purchase(self):
        return 'Tesco'

    def get_monthly_spending_amount(self):
        return 10

    def get_top_monthly_spending_category(self):
        return 'Shopping'

    def get_top_monthly_category_spend(self):
        return 10

    def get_yearly_spending_amount(self):
        return 10
