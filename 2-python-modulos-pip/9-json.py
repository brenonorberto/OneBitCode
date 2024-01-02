import json

# 1 - Strings para Dicionário
person = '{"name": "Breno", "languagens": ["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

# 2 - Converter dicionário para JSON
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

# 3 - Formatar JSON
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando JSON em txt
with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)

# 5 - Lendo JSON externo
with open('iris.json', 'r') as f:
    data = json.load(f)
    print(data)
