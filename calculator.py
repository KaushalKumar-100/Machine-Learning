"""Making a simple python console calculator 
using error handling and file Handling"""

HISTORY_FILE="calc_history.txt"

class Calculator :
    def __init__(self):
        self.history=self.load_history()
    
    def load_history(self):
        data=[]
        try:
            with open(HISTORY_FILE,"r") as f:
                for line in f:
                    line=line.strip()
                    if line:
                        data.append(line)
        except FileNotFoundError:
            pass
        return data
    def save_history(self):
        with open(HISTORY_FILE,"w") as f:
            for items in self.history:
                f.write(items+"n")
        
    def get_Numbers(self,message):
        while True:
            value=input(message)
            try:
                return float(value)
            
            except ValueError:   
                print("Enter a valid input") 
                       
               
                

    def add(self,a,b):
        return a+b
    
    def Sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        try:
            ans=a/b
            return ans
        except ZeroDivisionError:
            print("Divisor cannot be zero")
            return None
    
    def calculate(self,choice):
        a=self.get_Numbers("Enter the first Number:")
        b=self.get_Numbers("Enter the Second Numbers:")
        if choice=="1":
            result=self.add(a,b)
            op="+"
            
        elif choice=="2":
            result=self.Sub(a,b)
            op="-"
            
        elif choice=="3":
            result=self.mul(a,b)
            op="*"
            
        elif choice=="4":
            result=self.div(a,b)
            op="/"
            
        else:
            return
        if result is not None:
            record=f"{a}{op}{b}={result}"
            print("\n result is :",result)
            self.history.append(record)
            
        
    def show_history(self):
        if not self.history:
            print("no calculation yet")
            return
        print("\n The previous calculation is :")
        for items in self.history:
            print(items)
        
        
  
    
def main():
    calc=Calculator()
    while True:
        print("Simple calculator\n")
        print("1 Add")
        print("2 Subtract")
        print("3 multiplication")
        print("4 Divison")
        print("5 show History")
        print("6 Exit")
        choice=input("Enter the number you want to operate :")
        if choice in ["1","2","3","4"]:
            calc.calculate(choice)
        elif choice=="5":
            calc.show_history()
        elif choice =="6":
            calc.save_history()
            print("Goodbye! History is Saved")
            break
        else:
            print("Invalid choice")
            
            
             
if __name__=="__main__":
    main()
            
        
            