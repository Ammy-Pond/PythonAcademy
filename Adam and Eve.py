class Human:
    def __init__(self,name):
        self.name=name

class Woman(Human):
    def __init__(self, name):
        Human.__init__(self, name)

class Man(Human):
    def __init__(self, name):
        Human.__init__(self, name)

def God():
    my_list=[]
    Adam=Man('Adam')
    Eve=Woman('Eve')
    my_list.append(Adam)
    my_list.append(Eve)

    return my_list

paradise = God()
print(isinstance(paradise[0],Man))