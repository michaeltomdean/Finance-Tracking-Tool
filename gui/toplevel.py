from datetime import datetime
from tkinter import Label, Button, Toplevel, StringVar, Entry, OptionMenu
from PIL import Image, ImageTk
from tkcalendar import Calendar

from data.sql import FinanceSQL
from data.txt import Categories

from misc.tools import console_output, convert_month_id_to_str, get_year, get_month_id, is_float, convert_us_date_to_uk


class FinancialSummaryWindow(Toplevel):
    """
    Launch window to summarise finances
    """

    def __init__(self):
        """
        Initialise financial summary window.
        """
        super().__init__()
        self.title('Financial Summary')
        self.geometry('500x500')


class AddCategoryWindow(Toplevel):
    """
    Add categories to the categories text file
    """

    def __init__(self):
        """
        Initialise add category window
        """
        # Window Setup
        super().__init__()
        self.title('Add Category')
        self.geometry('350x250')
        self.resizable(height=False, width=False)

        # Title
        title_label = Label(self, text='Add Categories', font=('Arial', 20))
        title_label.place(x=100, y=10)

        # Images
        temp_image = Image.open(r"../assets/categories.png")
        temp_image = temp_image.resize((50, 50))
        self.categories_image = ImageTk.PhotoImage(temp_image)
        category_image_label = Label(self, image=self.categories_image)
        category_image_label.place(x=10, y=10)

        # Labels
        add_category_label = Label(self, text='Category Name', font=('Arial', 15))
        add_category_label.place(x=115, y=50)

        # Entry
        self.add_category_name = StringVar()
        add_category_entry = Entry(self, textvariable=self.add_category_name)
        add_category_entry.place(x=75, y=75)

        # Bottom
        add_category_button = Button(self, text='Add Category', command=self.add_category, width=15)
        add_category_button.place(x=115, y=125)

        # Exit Buttton
        exit_button = Button(self, text='Exit', command=self.destroy, width=15)
        exit_button.place(x=115, y=175)

    def add_category(self):
        """
        Add a category to the categories.txt file
        :return:
        """
        categories = Categories()
        if self.add_category_name.get() is not None and not (categories.check_duplicate(self.add_category_name.get())):
            categories.add(self.add_category_name.get())
            console_output('Category added!')
        else:
            console_output('Invalid category. Try again')


class RemoveCategoryWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Remove Category')
        self.geometry('350x150')
        self.resizable(height=False, width=False)

        title = Label(self, text='Remove Category', font=('Arial', 20))
        title.place(x=90, y=10)
        temp_image = Image.open(r'../assets/categories.png')
        temp_image = temp_image.resize((50, 50))
        self.categories_image = ImageTk.PhotoImage(temp_image)
        category_image_label = Label(self, image=self.categories_image)
        category_image_label.place(x=10, y=10)

        categories_label = Label(self, text='Select a category to remove', font=('Arial', 15))
        categories_label.place(x=90, y=50)

        self.categories_option = StringVar()
        self.categories_obj = Categories()
        categories_options = self.categories_obj.get().split('\n')
        categories_option_menu = OptionMenu(self, self.categories_option, *categories_options)
        categories_option_menu.place(x=150, y=75)

        ok_button = Button(self, text='Ok', command=self.delete_category, width=10)
        ok_button.place(x=115, y=100)
        exit_button = Button(self, text='Exit', command=self.destroy, width=10)
        exit_button.place(x=115, y=125)

    def delete_category(self):
        """
        Delete category from categories.txt file
        :return:
        """
        if self.categories_option.get() is not None or self.categories_option.get() != '':
            self.categories_obj.delete(self.categories_option.get())
            console_output('Category deleted')
        else:
            console_output('No category selected')


class MonthlyBudgetWindow(Toplevel):
    def __init__(self):
        """
        Initialise monthly budget window
        """
        # Window setup
        super().__init__()
        self.title('Monthly Budget Window')
        self.geometry('350x350')
        self.resizable(height=False, width=False)

        # Main Title
        monthly_budget_label = Label(self, text='Monthly Budget', font=('Arial', 20))
        monthly_budget_label.pack()

        # Picture
        temp_image = Image.open(r"../assets/calendar-icon.png")
        temp_image = temp_image.resize((50, 50))
        self.calendar_image = ImageTk.PhotoImage(temp_image)
        monthly_image_label = Label(self, image=self.calendar_image)
        monthly_image_label.place(x=10, y=10)

        # Labels
        current_month = convert_month_id_to_str(get_month_id())
        monthly_label = Label(self, text=f"Current Month: {current_month}")
        monthly_label.pack()

        # Button
        add_record_button = Button(self, text='Add Record', command=self.add_record, width=15)
        add_record_button.pack()
        remove_record_button = Button(self, text='Remove Record', command=self.remove_record, width=15)
        remove_record_button.pack()
        update_record_button = Button(self, text='Update Record', command=self.update_record, width=15)
        update_record_button.pack()
        view_monthly_spend_button = Button(self, text='View Monthly Spend', command=self.view_monthly_spend, width=15)
        view_monthly_spend_button.pack()
        view_category_spend_button = Button(self, text='View Category Spend', command=self.view_category_spend,
                                            width=15)
        view_category_spend_button.pack()
        exit_button = Button(self, text='Exit', command=self.exit, width=15)
        exit_button.pack()

    @staticmethod
    def add_record():
        """
        Launch add record window.
        :return:
        """
        window = AddRecordWindow()
        window.grab_set()

    @staticmethod
    def update_record():
        """
        Launch update record window.
        :return:
        """
        window = UpdateRecordWindow()
        window.grab_set()

    @staticmethod
    def remove_record():
        """
        Launch remove record window.
        :return:
        """
        window = RemoveRecordWindow()
        window.grab_set()

    @staticmethod
    def view_monthly_spend():
        """
        Launch view monthly spend window.
        :return:
        """
        window = ViewMonthlySpendWindow()
        window.grab_set()

    @staticmethod
    def view_category_spend():
        """
        Launch view category spend window.
        :return:
        """
        window = ViewCategorySpendWindow()
        window.grab_set()

    def exit(self):
        """
        Exit
        :return:
        """
        self.destroy()


class AddRecordWindow(Toplevel):
    """
    Add record window
    """

    def __init__(self):
        """
        Initialise add record window.
        """
        # Setup
        super().__init__()
        self.title('Add Record')
        self.geometry('500x500')
        self.resizable(height=False, width=False)
        self.date_window = None

        # Title
        title_label = Label(self, text='Add Record', font=('Arial', 20))
        title_label.pack()

        # Images
        temp_image = Image.open(r"../assets/finance.png")
        temp_image = temp_image.resize((50, 50))
        self.calendar_image = ImageTk.PhotoImage(temp_image)
        yearly_image_label = Label(self, image=self.calendar_image)
        yearly_image_label.place(x=10, y=10)

        # Labels
        transaction_name_label = Label(self, text='Transaction Name', font=('Arial', 15))
        transaction_name_label.place(x=185, y=50)

        transaction_amount_label = Label(self, text='Transaction Amount', font=('Arial', 15))
        transaction_amount_label.place(x=185, y=100)

        transaction_date_label = Label(self, text='Transaction Date', font=('Arial', 15))
        transaction_date_label.place(x=185, y=150)

        categories_label = Label(self, text='Transaction Category', font=('Arial', 15))
        categories_label.place(x=185, y=350)

        need_want_save_label = Label(self, text='Need? Want? Save?', font=('Arial', 15))
        need_want_save_label.place(x=185, y=400)

        # Entry
        self.transaction_name = StringVar()
        transaction_name_entry = Entry(self, textvariable=self.transaction_name)
        transaction_name_entry.place(x=150, y=75)

        self.transaction_amount = StringVar()
        transaction_amount_entry = Entry(self, textvariable=self.transaction_amount)
        transaction_amount_entry.place(x=150, y=125)

        self.date_entry = Calendar(self, selectmode='day', year=datetime.now().year,
                                   month=datetime.now().month, day=datetime.now().day)
        self.date_entry.place(x=125, y=175)

        # Options menu
        self.categories_option = StringVar()
        categories = Categories()
        categories_options = categories.get().split('\n')
        categories_option_menu = OptionMenu(self, self.categories_option, *categories_options)
        categories_option_menu.place(x=225, y=375)

        self.need_want_save_option = StringVar()
        need_want_save_options = ['Need', 'Want', 'Save']
        need_want_save_option_menu = OptionMenu(self, self.need_want_save_option, *need_want_save_options)
        need_want_save_option_menu.place(x=225, y=425)

        add_record_button = Button(self, text='Add Record', command=self.add_record, width=15)
        add_record_button.place(x=175, y=450)

        exit_button = Button(self, text='Exit', command=self.destroy, width=15)
        exit_button.place(x=175, y=475)

    def add_record(self):
        """
        Add record to the database.
        :return:
        """
        print(self.date_entry.selection_get())
        finance_sql = FinanceSQL()
        finance_sql.connect()
        if self.validate():
            finance_sql.add_spending_record(self.transaction_name.get(),
                                            self.categories_option.get(),
                                            self.date_entry.selection_get(),
                                            float(self.transaction_amount.get()),
                                            self.need_want_save_option.get())
        else:
            return

    def validate(self):
        """
        Validate inputs for record are correct.
        :return:
        """
        if self.need_want_save_option.get() == '':
            console_output('You have not selected the transaction type. Is it a need? A want? Or a saving?')
            return False
        if self.categories_option.get() == '':
            console_output('You have not selected a categories option')
            return False
        if self.transaction_amount.get() == '':
            console_output('You have not input a transaction amount')
            return False
        if not is_float(self.transaction_amount.get()):
            console_output('Your transaction amount is not an integer')
            return False
        if self.transaction_name.get() == '':
            console_output('You have not input a transaction name')
            return False
        return True


class UpdateRecordWindow(Toplevel):
    """
    Update record window.
    """

    def __init__(self):
        """
        Initialise record window.
        """
        super().__init__()
        self.title('Update Record')
        self.geometry('350x350')


class RemoveRecordWindow(Toplevel):
    """
    Remove record window.
    """

    def __init__(self):
        """
        Initialise view record window.
        """
        super().__init__()
        self.title('Remove Record')
        self.geometry('350x350')
        self.resizable(height=False, width=False)


class ViewMonthlySpendWindow(Toplevel):
    """
    View the months spending window.
    """

    def __init__(self):
        """
        Initialise months spending window.
        """
        # Window Setup
        super().__init__()
        self.title('View Monthly Spend')
        self.geometry('500x500')
        self.resizable(height=False, width=False)
        database = FinanceSQL()
        database.connect()

        # Title
        title_label = Label(self, text='View Monthly Spend', font=('Arial', 20))
        title_label.place(x=165, y=10)

        # Images
        temp_image = Image.open(r"../assets/finance.png")
        temp_image = temp_image.resize((50, 50))
        self.calendar_image = ImageTk.PhotoImage(temp_image)
        yearly_image_label = Label(self, image=self.calendar_image)
        yearly_image_label.place(x=10, y=10)

        # Labels
        current_monthly_spend = database.get_monthly_spending_amount()
        if current_monthly_spend is None:
            current_monthly_spend = 0
        current_monthly_spend = f"£{current_monthly_spend}"
        current_monthly_spend_label = Label(self, text='Current Monthly Spend:', font=('Arial', 15))
        current_monthly_spend_label.place(x=25, y=75)
        current_monthly_spend_total_label = Label(self, text=current_monthly_spend, font=('Arial', 15))
        current_monthly_spend_total_label.place(x=200, y=75)

        # Get top monthly category and top category spend data
        top_monthly_category, top_monthly_category_spend = database.get_top_monthly_spending_category()

        top_monthly_category_label = Label(self, text='Current Top Category:', font=('Arial', 15))
        top_monthly_category_label.place(x=25, y=100)
        top_monthly_category_variable_label = Label(self, text=top_monthly_category, font=('Arial', 15))
        top_monthly_category_variable_label.place(x=200, y=100)

        top_monthly_category_spend_label = Label(self, text='Top Category Spend:', font=('Arial', 15))
        top_monthly_category_spend_label.place(x=25, y=125)
        top_monthly_category_spend_variable_label = Label(self, text=top_monthly_category_spend, font=('Arial', 15))
        top_monthly_category_spend_variable_label.place(x=200, y=125)

        (last_monthly_purchase, last_monthly_purchase_amount,
         last_monthly_purchase_date) = database.get_last_monthly_purchase()
        last_monthly_purchase_date = convert_us_date_to_uk(last_monthly_purchase_date)

        last_monthly_purchase_label = Label(self, text='Last Purchase:', font=('Arial', 15))
        last_monthly_purchase_label.place(x=25, y=175)
        last_monthly_purchase_variable_label = Label(self, text=last_monthly_purchase, font=('Arial', 15))
        last_monthly_purchase_variable_label.place(x=200, y=175)

        last_monthly_purchase_amount_label = Label(self, text='Last Purchase Amount:', font=('Arial', 15))
        last_monthly_purchase_amount_label.place(x=25, y=200)
        last_monthly_purchase_amount_variable_label = Label(self, text=last_monthly_purchase_amount, font=('Arial', 15))
        last_monthly_purchase_amount_variable_label.place(x=200, y=200)

        last_monthly_purchase_date_label = Label(self, text='Last Purchase Date:', font=('Arial', 15))
        last_monthly_purchase_date_label.place(x=25, y=225)
        last_monthly_purchase_date_variable_label = Label(self, text=last_monthly_purchase_date, font=('Arial', 15))
        last_monthly_purchase_date_variable_label.place(x=200, y=225)
        # Plots
        # Entries


class ViewCategorySpendWindow(Toplevel):
    """
    View spending for individual categories
    """

    def __init__(self):
        super().__init__()
        self.title('View Category Spend')


class YearlyBudgetWindow(Toplevel):
    """
    View yearly finance information
    """

    def __init__(self):
        """
        Initialise yearly finance window.
        """
        # Window Setup
        super().__init__()
        self.title('Yearly Budget Window')
        self.geometry('350x350')
        self.resizable(height=True, width=False)

        # Main Title
        yearly_budget_label = Label(self, text='Yearly Budget', font=('Arial', 20))
        yearly_budget_label.pack()

        # Picture
        temp_image = Image.open(r"../assets/calendar-icon.png")
        temp_image = temp_image.resize((50, 50))
        self.calendar_image = ImageTk.PhotoImage(temp_image)
        yearly_image_label = Label(self, image=self.calendar_image)
        yearly_image_label.place(x=10, y=10)

        # Label
        current_year = get_year()
        yearly_label = Label(self, text=f"Current Year: {current_year}")
        yearly_label.pack()
