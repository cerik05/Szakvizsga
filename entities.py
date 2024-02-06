from random import randint

class Job:
    def __init__(self, id, title, department, salary, years, places):
        self.__title = title
        self.__id = id
        self.__department = department
        self.__salary = salary
        self.__years = years
        self.__places = places

    def get_title(self):
        return self.__title

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def get_years(self):
        return self.__years

    def get_places(self):
        return self.__places

    def set_title(self, new_title):
        self.__title = new_title

    def set_department(self, new_department):
        self.__department = new_department

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def set_years(self, new_years):
        self.__years = new_years

    def set_places(self, new_places):
        self.__places = new_places

    def __str__(self):
        return f"ID: {self.__id}, Title: {self.__title}, Department: {self.__department}, Salary: {self.__salary}, Experience: {self.__years}, Places left: {self.__places}"

class Applicant():
    __job_ids = list()

    def __init__(self, name, cv):
        self.__name = name
        self.__cv = cv

    def get_name(self):
        return self.__name

    def get_cv(self):
        return self.__cv

    def add_job(self, id):
        self.__job_ids.append(id)

    def get_job_ids(self):
        return self.__job_ids

    def __str__(self):
        return f"Name: {self.__name}, CV link: {self.__cv}, job_ids: {self.__job_ids}"