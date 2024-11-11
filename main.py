class Password:
    def __init__(self, acc, password):
        self.acc = acc
        self.password = password
        with open ("passwords.txt", "a") as x:
            x.write(f"Account: {self.acc},Password: {self.password}")
            
        
    def retrieve(self, acc_ret):
        print(self.password)
    
object_1 = Password("Github", "Password1")
object_2 = Password("Apple","Password2")

object_1.retrieve("Github")
object_2.retrieve("Apple")