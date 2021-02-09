class Students():
    def __init__(self, name, branch, year):
        super().__init__()
        self.name = name
        self.branch = branch
        self.year = year
        print("a student object is created")
    def printDetails(self):
        print(self.name)
        print(self.branch)
std1 = Students('ram',23,34)