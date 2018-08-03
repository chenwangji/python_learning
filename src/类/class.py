# coding = utf-8
# class C1:
#     def __init__(self, name):
#         self.name = name
#     def __del__(self):
#         print("goodbey ", self.name)
# c1 = C1('wangji')
# c1.__del__()

class Animal:
  color = 'red'
  name = ''
  def __init__(self, name):
    self.name = name
  def say(self):
    print('I can say')
  def intraduction(self):
    print('I am an animal, my name is %s.my skin color is %s'%(self.name, self.color))

animal = Animal('puppy')
animal.intraduction()

class Dog(Animal):
  color = 'green'
  name = ''
  def __init__(self, name):
    Animal.__init__(self, name)
  def intraduction(self):
    print('I am a dog, my name is %s.my skin color is %s'%(self.name, self.color))

dog = Dog('doggy')
dog.intraduction()
dog.say() # from super class

# 内省工具
print(dog.__class__)
print(dog.__class__.__name__)
print(dog.__dict__)