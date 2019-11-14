import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    all_user_story = []
    try:
        with open(DATA_FILE_PATH , 'r') as new_file:
            reader = csv.reader(new_file)
            import_data = list(reader)
            import_data.pop(0)
            for line in import_data:
                dict_temp = {}
                for i in range(len(DATA_HEADER)):
                    dict_temp[DATA_HEADER[i]] = line[i]
                all_user_story.append(dict_temp)
    except FileNotFoundError:
        print('File not found')
            
    return all_user_story
