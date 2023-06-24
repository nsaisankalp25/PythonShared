class FileManager():
    def __init__(self):
        pass

    def WriteToFile(self, info):
        self.info = info
        with open(r"PATH\todolist.txt", "a") as file:
            file.write(self.info + "\n")
            
    def ReadFile(self):
        with open(r"PATH\todolist.txt", "r") as file:
            self.items = file.read().strip()
        return self.items
    
class UserTalk(FileManager):
    def __init__(self):
        super().__init__()
        print("Welcome to the To-Do List Application done with OOPS Python")
        print("Enter 1 - Add a Task \n Enter 2 - View Tasks")
        self.ask = input("")
        if self.ask.strip() == '1':
            self.AddTask()
        
        elif self.ask.strip() == '2':
            self.ViewTasks()
        
        else:
            print("Only Enter 1 or 2")

    def AddTask(self):
        print("Enter the Task in Brief")
        self.task = input("")
        self.task = self.task.strip()
        self.WriteToFile(self.task)
        print("Task Added!")
    
    def ViewTasks(self):
        print("Here are your Tasks!")
        print("---")
        print(self.ReadFile())
        print("---")

obj = UserTalk()

    
