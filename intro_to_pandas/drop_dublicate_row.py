import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])


if __name__ == '__main__':
    col = ['name', 'salary', 'email']
    data = [
        ['piper', 4548, 'abc@yopmail.com'],
        ['Grace', 28150, 'test1@yopmail.com'],
        ['Georgia', 1000, 'a@yopmail.com'],
        ['willow', 1000, 'a@yopmail.com'],
        ['Finn', 74576, 'test@yopmail.com'],
    ]
    bonus = dropDuplicateEmails(pd.DataFrame(data, columns=col))
    print(bonus)
