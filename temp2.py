class tmp:
    name = "TD"
    def prnt(self):
        print(self.name)
        
obj = tmp()

obj.name = "Hello"
print(obj.prnt)

obj.prnt()