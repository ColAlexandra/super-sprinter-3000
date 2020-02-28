import csv
import os
from typing import Any

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    all_user_story = []
    try:
        with open(DATA_FILE_PATH , 'r') as new_file:
            reader = csv.reader(new_file)
            import_data = list(reader)
            print(import_data)
            import_data.pop(0)
            for line in import_data:
                dict_temp = {}
                for i in range(len(DATA_HEADER)):
                    dict_temp[DATA_HEADER[i]] = line[i].replace('<br>', '\n')
                all_user_story.append(dict_temp)
    except FileNotFoundError:
        print('File not found')
    return all_user_story


def export_file(list_dict):
    try:
        with open(DATA_FILE_PATH, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=DATA_HEADER)
            writer.writeheader()
            print(list_dict)
            for data in list_dict:
                print(data)
                writer.writerow(data)
    except PermissionError:
        print('File not found')


def export_to_file(title, user_story, acceptance_criteria, business_value, estimation, status):
    list_dict = add_dictionary_to_file(title, user_story, acceptance_criteria, business_value, estimation, status)
    export_file(list_dict)

def export_update(title, user_story, acceptance_criteria, business_value, estimation, status, id):
    list_dict = add_update_dictionary_to_file(title, user_story, acceptance_criteria, business_value, estimation, status, id)
    print(list_dict)
    export_file(list_dict)

def new_id_story():
    user_stories = get_all_user_story()
    id_list = []
    for story in user_stories:
        for id in story['id']:
            id_list.append(int(id))
    for i in range(len(sorted(id_list))):
        if i not in id_list:
            return i

    return len(id_list)


def new_dictionary(title, user_story, acceptance_criteria, business_value, estimation, status):
    user_stories = get_all_user_story()
    titles = user_stories[0]
    headers = [key for key, values in titles.items()]
    new_dict = {}
    new_id = new_id_story()
    for header in headers:
        new_dict[header] = 0
    for key, values in new_dict.items():
        if key == 'title':
            new_dict[key] = title
        if key == 'user_story':
            new_dict[key] = user_story
        if key == 'acceptance_criteria':
            new_dict[key] = acceptance_criteria
        if key == 'business_value':
            new_dict[key] = business_value
        if key == 'estimation':
            new_dict[key] = estimation
        if key == 'status':
            new_dict[key] = status
        if key == 'id':
            new_dict[key] = new_id
    return new_dict

def update_dictionary(title, user_story, acceptance_criteria, business_value, estimation, status,id):
    user_stories = get_all_user_story()
    titles = user_stories[0]
    headers = [key for key, values in titles.items()]
    new_dict = {}
    choose_story_id(id)
    for header in headers:
        new_dict[header] = 0
    for key, values in new_dict.items():
        if key == 'title':
            new_dict[key] = title
        if key == 'user_story':
            new_dict[key] = user_story
        if key == 'acceptance_criteria':
            new_dict[key] = acceptance_criteria
        if key == 'business_value':
            new_dict[key] = business_value
        if key == 'estimation':
            new_dict[key] = estimation
        if key == 'status':
            new_dict[key] = status
        if key == 'id':
            new_dict[key] = id
    return new_dict


def choose_story_id(id):
    user_stories = get_all_user_story()
    user_story =[]
    for story in user_stories:
        if story['id'] == id:
            user_story.append(story)
    return user_story[0]
            

def add_dictionary_to_file(title, user_story, acceptance_criteria, business_value, estimation, status):
    list_dict = get_all_user_story()
    new_dict = new_dictionary(title, user_story, acceptance_criteria, business_value, estimation, status)
    list_dict.append(new_dict)
    return list_dict

def add_update_dictionary_to_file(title, user_story, acceptance_criteria, business_value, estimation, status, id):
    new_list = get_all_user_story()
    list_dict = []
    skip = False
    for dict in new_list:
        if dict['id'] != id:
            list_dict.append(dict)
    print(list_dict)
    new_dict = update_dictionary(title, user_story, acceptance_criteria, business_value, estimation, status, id)
    list_dict.append(new_dict)
    return list_dict

