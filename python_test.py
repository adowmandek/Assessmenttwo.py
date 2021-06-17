x = [100,110,120,130,140,150]
new_list = []
for a in x:
    new_list.append(x*5)
    print(new_list)

def divisible_by_three(n):
    n=range(1,10)
    for y in n:
        if y%3==0:
            print(y)

def name():
    x = [[1,2],[3,4],[5,6]]
    list(flatten(x))


def smallest(X):
    y=max(X)
    if y <1:
        return 1


def listed(x):
        x = ['a','b','a','e','d','b','c','e','f','g','h']
        h=['i','j','k','l','m','n','o','p','q','r','s']
        h.remove(x)
        print(h)





# def divisible_by_seven():
#     n=range(1,100)
#     for s in n:
#         if s%7==0:
#             print(s)


def students():
    names="Eunice", "Agnes","Teresa","Asha"
    ages=19,21,18,22
    print(f"hello my name is {name} and i am{age} years old ")
    print(f"hello my name is{name} and i am  {age} years old")
    print(f"hello my name is{name} and i am  {age}years old ")
    print(f"hello my name is {name} and i am {age}years old ")


    students()



class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(18,10)
print(newRectangle.rectangle_area())






