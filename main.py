import emoji

from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(f'Current date: {datetime.today().strftime("%d-%m-%Y")}')
    calculate_salary('Petrov')
    get_employees('Ivanov')
    print(emoji.emojize(':thumbs_up:'))