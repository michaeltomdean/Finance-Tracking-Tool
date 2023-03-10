from tkinter.ttk import Label, Button
from tkinter import messagebox
from PIL import Image, ImageTk
from gui.toplevel import MonthlyBudgetWindow, YearlyBudgetWindow, FinancialSummaryWindow, \
    AddCategoryWindow, RemoveCategoryWindow
from misc.tools import ver, author, console_output
from ttkthemes import ThemedTk


class HomeWindow(ThemedTk):
    """
    Main window of the program. Runs in the mainloop of tkinter and launches all toplevel ui elements.
    """
    def __init__(self):
        """
        Initialise the window with tkinter parameters, labels, buttons, images etc
        :return:
        """
        super().__init__(background=True)
        self.set_theme(theme_name='equilux')
        self.title('Home')
        self.geometry('600x250')
        self.resizable(height=False, width=False)

        # Themes

        # Title Label
        title_label = Label(self, text='Home', font=('Arial', 20))
        title_label.place(x=275, y=10)

        # Finance
        # Labels
        finance_label = Label(self, text='Finance', font=('Arial', 15))
        finance_label.place(x=125, y=65)

        # Buttons
        monthly_budget_button = Button(self, text='Monthly Budget', command=self.monthly_budget, width=16)
        monthly_budget_button.place(x=25, y=100)
        yearly_budget_button = Button(self, text='Yearly Budget', command=self.yearly_budget, width=16)
        yearly_budget_button.place(x=150, y=100)
        investments_button = Button(self, text='Investments', command=self.investments, width=16)
        investments_button.place(x=25, y=125)
        summary_button = Button(self, text='Summary', command=self.summary, width=16)
        summary_button.place(x=150, y=125)
        recalculate_button = Button(self, text='Recalculate', command=self.recalculate, width=16)
        recalculate_button.place(x=25, y=150)

        # Pictures
        temp_image = Image.open(r"../assets/finance.png")
        temp_image = temp_image.resize((50, 50))
        self.finance_image = ImageTk.PhotoImage(temp_image)
        finance_image_label = Label(self, image=self.finance_image)
        finance_image_label.place(x=10, y=10)

        # Settings
        # Labels
        settings_label = Label(self, text='Settings', font=('Arial', 15))
        settings_label.place(x=400, y=65)

        # Buttons
        show_info_button = Button(self, text='Show Info', command=self.show_info, width=16)
        show_info_button.place(x=325, y=100)
        setup_button = Button(self, text='Setup Databases', command=self.setup, width=16)
        setup_button.place(x=450, y=100)
        add_categories_button = Button(self, text='Add Category', command=self.add_category, width=16)
        add_categories_button.place(x=325, y=125)
        remove_categories_button = Button(self, text='Remove Category', command=self.remove_category, width=16)
        remove_categories_button.place(x=450, y=125)

        # Pictures
        temp_image = Image.open(r"../assets/settings.png")
        temp_image = temp_image.resize((50, 50))
        self.settings_image = ImageTk.PhotoImage(temp_image)
        settings_image_label = Label(self, image=self.settings_image)
        settings_image_label.place(x=490, y=10)

        # Buttons
        exit_button = Button(self, text='Exit Button', command=self.exit, width=16)
        exit_button.place(x=235, y=200)

    @staticmethod
    def show_info():
        """
        Show author and version of the program
        :return:
        """
        messagebox.showinfo("Info", f"Version: {ver()} \n Author: {author()}")

    @staticmethod
    def monthly_budget():
        """
        Launch monthly budget window
        :return:
        """
        window = MonthlyBudgetWindow()
        window.grab_set()

    def setup(self):
        """
        Setup the program.
        :return:
        """
        pass

    @staticmethod
    def yearly_budget():
        """
        Launch yearly budget window.
        :return:
        """
        window = YearlyBudgetWindow()
        window.grab_set()

    @staticmethod
    def recalculate():
        """
        Recalculate local values and datapoints.
        :return:
        """
        console_output('Recalculated Values')
        messagebox.showinfo('Done', 'Recalculated datapoints')

    @staticmethod
    def add_category():
        """
        Launch add categories window.
        :return:
        """
        window = AddCategoryWindow()
        window.grab_set()

    @staticmethod
    def remove_category():
        """
        Launch remove categories window
        :return:
        """
        window = RemoveCategoryWindow()
        window.grab_set()

    @staticmethod
    def summary():
        """
        Launch summary window.
        :return:
        """
        window = FinancialSummaryWindow()
        window.grab_set()

    def investments(self):
        """
        Launch investments window.
        :return:
        """
        pass

    def ok(self):
        """
        ?
        :return:
        """
        pass

    def exit(self):
        """
        Exit from window
        :return:
        """
        self.destroy()
