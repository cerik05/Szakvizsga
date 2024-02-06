from entities import Job
from entities import Applicant
from random import randint

class Service():
    __joblist = []
    __applicantlist = []
    def __init__(self):
        pass

    def add_job(self):
        job = input("Title: ")
        job1 = randint(1, 9999999999)
        job2 = input("Department: ")
        job3 = input("Salary: ")
        job4 = input("Years of experience: ")
        job5 = input("Places left: ")
        new = Job(job1, job, job2, job3, job4, job5 )
        self.__joblist.append(new)

    def find_position_of_job(self, __joblist, id):
        for i in range(len(self.__joblist)):
            print(self.__joblist[i].get_id())
            if str(self.__joblist[i].get_id()) == str(id):
                return i
        return -1

    def remove_job(self):
        for job in self.__joblist:
            print(str(job))
        id = input("Which job would you like to delete?(id) ")
        position = self.find_position_of_job(self.__joblist, id)
        if position != -1:
            del self.__joblist[position]
            print(f"Job with the id of {id} was deleted!")
        else:
            print(f"Job with the id of {id} not found!")

    def specific_jobs(self):
        for job in self.__joblist:
            print(str(job))
        department = input("Choose a department: ")
        for job in self.__joblist:
            if job.get_department() == department:
                print(str(job))

    def applicant_information(self):
        for i in self.getjoblist():
            print(str(i))
        job1 = input("Job ID: ").strip()
        name = input("Name: ")
        cv = input("CV link: ")
        new = Applicant(name, cv)
        new.add_job(job1)
        self.__applicantlist.append(new)
        for job in self.__joblist:
            if int(job.get_places()) > 0:
                self.__applicantlist.append(new)
                self.lower_places(job1)
                break
            else:
                print("There are no free places in this Job")

    def job_applicants(self):
        for i in self.getjoblist():
            print(str(i))
        job_id = input("Choose a job ID: ")
        for applicant in self.getapplicantlist():
            for id in applicant.get_job_ids():
                if str(id) == str(job_id):
                    print(str(applicant))
                    break


    def lower_places(self, id):
        for job in self.__joblist:
            if str(job.get_id()) == str(id):
                job.set_places(int(job.get_places()) - 1)

    def bubbleSort(self, arr):
        n = len(arr)
        swapped = False
        for i in range(n - 1):
           for j in range(0, n - i - 1):
                if arr[j].get_salary() > arr[j + 1].get_salary():
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

           if not swapped:
               return



    def getjoblist(self):
        return self.__joblist

    def getapplicantlist(self):
        return self.__applicantlist