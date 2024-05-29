from abc import ABC, abstractmethod
from termcolor import colored
from prettytable import PrettyTable 

class Bot(ABC):
    
    @abstractmethod
    def return_all_users(self, book):
        pass

    @abstractmethod
    def format_display(self, text):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def birthdays_congratulate(self, list):
        pass

"""
Colorize text.

Available text colors:
    black, red, green, yellow, blue, magenta, cyan, white, light_grey, dark_grey, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan.

Available text highlights:
    on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white, on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow, on_light_blue, on_light_magenta, on_light_cyan.

Available attributes:
    bold, dark, underline, blink, reverse, concealed.

Example:
    colored('Hello, World!', 'red', 'on_black', ['bold', 'blink']) colored('Hello, World!', 'green')
"""

class ColorBot(Bot):
    def return_all_users(self, book):
        return colored(book, 'blue')
    
    def format_display(self, text):
        return colored(text, 'blue')
    
    def __str__(self):
        return f"Activated Color bot"
    
    def birthdays_congratulate(self, list):
        return colored(list, 'blue')

    

class TableBot(Bot):
    def return_all_users(self, book):
            
        adress_list=[]
        i = 0
        while i <= len(list(book))-1:
            item=[]
            item.append(list(book)[i])
            record = book.find(list(book)[i])
            item.append(record.phone_list())
            item.append(record.birthday)
            adress_list.append(item)
            i += 1

        myTable = PrettyTable(["Contact Name", "Phones", "Birthday"])
        for item in adress_list:
            myTable.add_row(item)
        return myTable 

    
    def format_display(self, text):
        myTable = PrettyTable([text])
        return myTable
    
    def __str__(self):
        return "Activated Table bot"
    
    def birthdays_congratulate(self, list):

        birthday_list=[]
        i = 0
        while i <= len(list)-1: 
            item=[]
            item.append(list[i]['name'])
            item.append(list[i]['congratulation_date'])
            birthday_list.append(item)
            i += 1

        myTable = PrettyTable(["Name", "Congratulation Date"])
        for item in birthday_list:
            myTable.add_row(item)
        return myTable 

    


class StandardBot(Bot):
    def return_all_users(self, book):
        return book
    
    def format_display(self, text):
        return text
    
    def __str__(self):
        return "Activated Standard bot"
    
    def birthdays_congratulate(self, list):
        return list

