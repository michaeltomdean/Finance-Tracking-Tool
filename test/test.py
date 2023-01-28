from data.sql import FinanceSQL
from data.txt import Categories
from gui.mainloop import HomeWindow


def homewindow():
    home = HomeWindow()
    home.mainloop()


if __name__ == '__main__':
    # homewindow()
    database = FinanceSQL()
    print(database.get_top_monthly_spending_category())

