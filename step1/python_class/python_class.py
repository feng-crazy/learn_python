# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""
from abc import abstractmethod, ABCMeta


class Student(object):
    teacher = 'my_123'

    def __init__(self, student_name):
        self._score = 99
        self._student_name = student_name
        self._age = 18

    @property
    def student_name(self):
        print('student name property')
        return self._student_name

    @student_name.setter
    def student_name(self, student_name):
        print('student_name.setter')
        self._student_name = student_name

    @student_name.getter
    def student_name(self):
        print('student_name.getter')
        return self._student_name

    @property
    def age(self):
        print('property age ')
        return self._age

    @abstractmethod
    def get_score(self):
        return self._score


class hedengfeng(Student):
    iq = 180

    def __init__(self, student_name):
        super(hedengfeng, self).__init__()
        self._score = 59
        # self._student_name = student_name

    def get_score(self):
        return self._score

    def set_iq(self, value):
        self.iq = value

    def msg_handle(self, key):
        func = self.msg_handle_table[key]
        print('msg_handle result:')
        print(func(self))

    msg_handle_table = {'get_score': get_score, 'set_id': set_iq}


if __name__ == '__main__':
    student_name = 'sb'
    student = Student(student_name)
    print(student.student_name)
    # student.student_name = 'hdf' # no
    student.student_name = 'hdf'
    print(student.student_name)
    # student.age = 26
    print(student.age)
    print(student.get_score())

    student1 = hedengfeng('hedengfeng')
    print(student1.get_score())

    print('```````````````````````````````````')
    print(student1.iq)
    # student1.iq = 220
    student1.set_iq(230)
    print(hedengfeng.iq)
    hdf = hedengfeng('hdf')
    hdf._score = 99
    print(hdf.iq)

    hdf.eq = 300
    print(hdf.eq)

    hdf.msg_handle('get_score')

    func = hedengfeng.msg_handle_table['get_score']
    hdf_score = func(hdf)
    print(hdf_score)

    terminal_msg_table = {'hdf': hdf, 'hedengfeng': student1}
    my_score = func(terminal_msg_table['hdf'])
    print(my_score)
    my_score = func(terminal_msg_table['hedengfeng'])
    print(my_score)
    terminal_msg_table['shuaige'] = 123
    print(terminal_msg_table)
