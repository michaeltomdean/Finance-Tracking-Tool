from datetime import datetime


def console_output(string: str):
    print(f"Info -> {string}")


def ver():
    return 'v0.1a'


def author():
    return 'Michael Dean'


def get_month_id():
    return datetime.now().month


def get_year():
    return datetime.now().year


def convert_month_id_to_str(id: int):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'Novemeber',
        'December',
    ]
    return months[id - 1]


def get_user_data_path():
    return r"/Users/michael/Library/Application Support/finance-tracking/userdata"


def get_monthly_image_path():
    month_id = get_month_id()
    picture_map = {
        1: 'jan.png',
        2: 'feb.png',
        3: 'mar.png',
        4: 'apr.png',
        5: 'may.png',
        6: 'jun.png',
        7: 'jul.png',
        8: 'aug.png',
        9: 'sep.png',
        10: 'oct.png',
        11: 'nov.png',
        12: 'dec.png',
    }
    picture_path = rf"\assets\monthly_picture\{picture_map[month_id]}"
    return picture_path


def is_float(number: str):
    try:
        float(number)
    except ValueError:
        return False
    else:
        return True


def convert_us_date_to_uk(date: str):
    """
    :param date: US date as string
    :return: UK data format dd-mm-yyyy
    """
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    return f"{day}-{month}-{year}"



