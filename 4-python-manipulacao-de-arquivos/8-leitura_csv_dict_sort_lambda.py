courses = []

with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        courses.append({
            'language': language,
            'category': category
        })
print(courses)


for course in sorted(courses, key=lambda course: course['language']):
    print(f'{course["language"]} - {course["category"]}')
