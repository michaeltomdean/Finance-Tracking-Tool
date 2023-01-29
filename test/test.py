from data.sql import FinanceSQL
from data.txt import Categories
from gui.mainloop import HomeWindow
from misc.tools import convert_us_date_to_uk


def homewindow():
    home = HomeWindow()
    home.mainloop()


if __name__ == '__main__':
    homewindow()
