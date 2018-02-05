import json


class Student(object):
    def __init__(self, json_dict):
        self.id = json_dict['id']
        self.name = json_dict['name']
        self.age = json_dict['age']


def load_to_db(json_str, db):
    print(json_str)
    student_dict = json.loads(json_str)

    for id, info in student_dict.iteritems():
        student = Student(info)
        _add_to_db(student, db)


def _add_to_db(student, db):
    INSERT_QUERY = '''
        INSERT INTO students (
            id,
            name,
            age
        ) values (?, ?, ?)
    '''
    db.execute(INSERT_QUERY,
                         (student.id, student.name, student.age))



