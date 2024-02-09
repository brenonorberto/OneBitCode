courses = []

with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        courses.append({
            'language': language,
            'category': category
        })
print(courses)


def get_language(course):
    return course['language']


def get_category(course):
    return course['category']


for course in sorted(courses, key=get_language, reverse=True):
    print(f'{course["language"]} - {course["category"]}')
