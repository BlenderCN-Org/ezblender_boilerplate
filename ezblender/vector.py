class Vector:
    def __init__(self,values):
        if(type(values)==tuple):
            self.values = values
        elif(type(values)==list):
            self.values = tuple(values)
        elif(values.__class__.__name__=='Euler'):
            # TODO Other orderings
            self.values = (values.x,values.y,values.z)
        elif(values.__class__.__name__=='BMVert'):
            self.values = (values.co.x,values.co.y,values.co.z)
        elif(values.__class__.__name__=='Vector'):
            if values.__class__==Vector:
                self.values = values.values
            else:
                self.values = (values.x,values.y,values.z)
        elif(values.__class__.__name__=='Quaternion'):
            self.values = (values.w,values.x,values.y,values.z)
        else:
            raise Exception('Unknown vector class: '+values.__class__.__name__)
    
    def __add__(self,other):
        return Vector([x+y for x,y in zip(self.values,other.values)])
    def __sub__(self,other):
        return Vector([x-y for x,y in zip(self.values,other.values)])

    def __len__(self):
        return len(self.values)

    def __ne__(self,other):
        return not self.__eq__(other)

    def __eq__(self,other):
        return self.values == Vector(other).values

    def __getattr__(self,name):
        if name == 'x': 
            return self.__dict__['values'][len(self)-3]
        elif name == 'y': 
            return self.__dict__['values'][len(self)-2]
        elif name == 'z': 
            return self.__dict__['values'][len(self)-1]
        elif name =='w':
            return self.__dict__['values'][0]
        else:
            return self.__dict__[name]

    def __setattr__(self,name,value):
        if name == 'x': 
            self.__dict__['values'][len(self)-3] = value
        elif name == 'y': 
            self.__dict__['values'][len(self)-2] = value
        elif name == 'z': 
            self.__dict__['values'][len(self)-1] = value
        elif name == 'w':
            self.__dict__['values'][0] = value
        else:
            self.__dict__[name] = value

    def __repr__(self):
        return self.values.__repr__()