
RECORD_DATA="RecordofStudent.txt"

class StudentManager:
    def __init__(self):
        self.history=self.load_record()
        
    def load_record(self):
        record={}
        try:
            with open(RECORD_DATA,"r") as file:
                for line in file:
                    line=line.strip()
                    if line:
                        name,marks=line.split(":")
                        record[name]=float(marks)
                        
        except FileNotFoundError:
            pass
        return record
                
    def show_record(self):
        if not self.history:
            print("No Student added yet")
            print("\n")
            return
        else:
            print("previous record are: ")
            for item in self.history:
                print(item)
                
    def save_record(self):
        
        with open(RECORD_DATA,"w") as file:
            for name,marks in self.history.items():
                file.write(f"{name} : {marks}\n")
            
    def get_marks(self):
        while True:
            value=input("enter your marks:")
            try:
                return float(value)
            except ValueError:
                print("Enter a valid number:")               
    
    def add_student(self):
        name=input("Enter your Name: ")
        if name in self.history:
            print("Name already exits\n")
            return
        marks=self.get_marks()
        self.history[name]=marks
        print("Student added successfully\n")
        
    
    def delete_student(self):
        name=input("Enter the name of student:\n")
        if name in self.history:
            del self.history[name]
            print("Student Deleted")
        else:
            print("Student not found\n")
        
    def search_student(self):
        name=input("Enter the Name of your student:")
        if name not in self.history:
            print("Name not Found\n")
        else:
            print(name ,":",self.history[name])
        
    def update_student(self):
        name=input("Enter the name of student:")
        if name in self.history:
            marks=self.get_marks()
            self.history[name]=marks
            print("The updated student marks is ",name,":",self.history[name])
        
    def view_record(self):
        if not self.history:
            print("No any record Find\n")
            
        for name,marks in self.history.items():
            print(name," : ",marks)

def main():
    manager=StudentManager()
    while True:
        print("Choose one from which operation do you want to perform:\n")
        
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_record()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            manager.save_record()
            print("Goodbye. Records saved.")
            break
        else:
            print("Invalid choice. Try again.")
            
if __name__=="__main__":
    main()