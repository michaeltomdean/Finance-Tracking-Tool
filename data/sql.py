import sqlite3
from datetime import datetime

from data.txt import Categories
from misc.tools import get_user_data_path
from calendar import monthrange


class FinanceSQL:
    def __init__(self):
        self.path = fr"{get_user_data_path()}/finance.db"
        self.connection, self.cursor = self.connect()
        self.first_month_date, self.last_month_date = self.calculate_last_first_month_dates()
        self.current_date = f"{datetime.now().year}-{datetime.now().month:02d}-{datetime.now().day:02d}"

    def connect(self):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        return connection, cursor

    @staticmethod
    def calculate_last_first_month_dates():
        _, last_day = monthrange(datetime.now().year, datetime.now().month)  # Calculates days in month.
        first_month_date = f"{datetime.now().year}-{datetime.now().month:02d}-01"  # Format numbers eg 1 into 01
        last_month_date = f"{datetime.now().year}-{datetime.now().month:02d}-{last_day:02d}"
        return first_month_date, last_month_date

    def get_all_spending(self):
        self.cursor.execute("""
        SELECT * FROM spending
        """)
        return self.cursor.fetchall()

    def get_all_monthly_spending(self):
        self.cursor.execute(
            """
            SELECT *
            FROM spending
            WHERE datetime between ? and ?
            """,
            (self.first_month_date, self.last_month_date))
        data = self.cursor.fetchall()
        if not data:
            return None
        else:
            return data

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
        """
        Calculates last monthly purchase name, amount and date
        :return: name, amount, data
        """
        self.cursor.execute(
            """
            SELECT name, amount, datetime
            FROM spending
            WHERE datetime < ?
            ORDER BY datetime DESC
            """,
            [self.current_date], )  # Singular values need the comma + strings need to be inputted as lists
        data = self.cursor.fetchall()
        if not data:
            return None
        else:
            data = data[0]
            name, amount, date = data[0], data[1], data[2]
            return name, amount, date

    def get_monthly_spending_amount(self):
        self.cursor.execute(
            """
            SELECT SUM(amount)
            FROM spending
            WHERE datetime between ? and ?
            """,
            (self.first_month_date, self.last_month_date))
        data = self.cursor.fetchall()
        print(data)
        if not data:
            return None
        else:
            return data[0][0]

    def get_top_monthly_spending_category(self):
        """
        Calculates category with the highest transaction amount. If no categories are found returns None None
        :return: category, amount_spent
        """
        categories = Categories()
        categories_list = categories.get().split('\n')
        categories_list = [x for x in categories_list if x != '']
        category_spend = {}

        # Loop through all categories, sum the spend on each, append to dictionary
        for category in categories_list:
            self.cursor.execute(
                """
                SELECT SUM(amount)
                FROM spending
                WHERE datetime between ? and ? and category=?
                """,
                (self.first_month_date, self.last_month_date, category))

            # Identify if there are any purchases in this category. An empty list [] will return true to not list
            data = self.cursor.fetchall()
            if not data:
                continue
            else:
                data = data[0]
                category_spend[f"{category}"] = data

        # If the dictionary is empty. There are no purchases this month. Therefore return None
        if category_spend == {}:
            return None, None

        # Find maximum key and value
        values = list(category_spend.values())
        keys = list(category_spend.keys())
        max_value = max(category_spend.values())
        max_key = keys[values.index(max(values))]

        return max_key, max_value[0]

    def get_yearly_spending_amount():
        return 10
