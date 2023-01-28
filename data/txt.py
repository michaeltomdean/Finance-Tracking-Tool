from misc.tools import get_user_data_path


class Categories:
    def __init__(self):
        self.path = fr"{get_user_data_path()}/categories.txt"

    def get(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    def add(self, category: str):
        with open(self.path, 'a') as file:
            file.write(category+'\n')

    def delete(self, category: str):
        with open(self.path, 'r+') as file:
            data = file.readlines()
            file.seek(0)
            for x in data:
                if x != category:
                    file.write(x)
            file.truncate()

    def check_duplicate(self, category: str):
        data = self.get()
        if category not in data:
            return False
        else:
            return True
