class employee:
    def __init__(self, name, idNum, department, jobTitle, monthlySalary):
        self.__name = name
        self.__idNum = idNum
        self.__department = department
        self.__jobTitle = jobTitle
        self.__monthlySalary = monthlySalary


    def setName(self,name):
        self.__name = name

    def setIdNum(self,idNum):
        self.__idNum = idNum

    def setDepartment(self,department):
        self.__department = department

    def setJobTitle(self,jobTitle):
        self.__jobTitle = jobTitle

    def setMonthlySalary(self,monthlySalary):
        self.__monthlySalary = monthlySalary



    def getName(self):
        return self.__name

    def getIdNum(self):
        return self.__idNum

    def getDepartment(self):
        return self.__department

    def getJobTitle(self):
        return self.__jobTitle

    def getMonthlySalary(self):
        return self.__monthlySalary