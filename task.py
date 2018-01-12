import json
import pprint

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        json_file = open("data.json", "r")
        f= json_file.read()
        data = json.loads(f)

except FileExistsError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'


for index, i in enumerate(data):
    print('\nData number in the list №', index)

    a = {}
    a.update(
	{'address':i.get('address')})
    pprint.pprint(a)

    b = {}
    b.update(
        {'company': i.get('company'),
         'email': i.get('email'),
         'phone': i.get('phone')})
     pprint.pprint(b)
