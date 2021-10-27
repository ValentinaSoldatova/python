result_dict = {}
with open('5.6_file.txt') as file:
    for line in file:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip('(Л)(ПР)(КР)')) for lesson in lessons if lesson != '-']
        result_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})
print(result_dict)

