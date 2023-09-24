import emoji

from datetime import *

from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print(f'Current date: {datetime.today().strftime("%d-%m-%Y")}')
    calculate_salary('Petrov')
    get_employees('Ivanov')
    print(emoji.emojize(':thumbs_up:'))