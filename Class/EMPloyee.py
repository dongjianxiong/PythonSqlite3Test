# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Person(object):
    def __init__(self, uid, name, age, gender):
        self.uid = uid
        self.name = name
        self.age = age
        self.gender = gender

    def displayEmployee(self):
        print("UID : ", self.uid, "Name : ", self.name, " Age: ", self.age, " Gender: ", self.gender)

class Employee(Person):
    '所有员工的基类'
    empCount = 0

    def __init__(self, uid, name, age, gender, address, salary):
        super(Employee, self).__init__(uid, name, age, gender)
        self.address = address
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("UID : ", self.uid, "Name : ", self.name, " Age: ", self.age, " Gender: ", self.gender, " Address: ", self.address, " Salary: ", self.salary)