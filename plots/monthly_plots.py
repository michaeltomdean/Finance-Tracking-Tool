from matplotlib import pyplot as plt
from data.sql import FinanceSQL
import numpy as np


def plot_monthly_category_spend():
    database = FinanceSQL()
    data = database.get_all_monthly_spending()
    print(data)

    # Check if data is not none. If so do plot. Else return None
    categories = {}
    if data is not None:

        # Iterate through all the data and sum up the spending for each category
        for record in data:
            transaction_id, name, category, datetime, amount, type = record

            # Add all categories and then amount sum values to a dictionary
            if category not in categories.keys():
                categories[f'{category}'] = amount
            elif category in categories.keys():
                total = categories[f'{category}'] + amount
                categories[f'{category}'] = total
            else:
                raise ValueError('Error in dictionary values')  # Raise should not occur.
    else:
        return None

    # Plot data
    fig, ax = plt.subplots()
    x = np.arange(0, len(categories.keys()), 1)
    data = categories.values()
    keys = [key for key in categories.keys()]
    ax.bar(x, height=data, width=0.35)
    plt.xlabel('Monthly Category Spend')
    plt.ylabel('Amount £')
    plt.xticks(x, keys)
    for i, value in enumerate(data):
        plt.annotate(value, (i, value))
    plt.show()


def plot_month_on_month_spend():
    pass


plot_monthly_category_spend()
