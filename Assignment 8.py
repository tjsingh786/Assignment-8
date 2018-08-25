#ques1
class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        self.ar=3.14*self.radius*self.radius
        print(self.ar)
    def circumfrence(self):
        self.cir=2*3.14*self.radius
        print(self.cir)
c=circle(3)
c.area()
c.circumfrence()

#ques2
class student():
      def __init__(self,person_name,person_rno):
          self.name=person_name
          self.rno=person_rno
      def age(self,person_age):
          self.age=person_age
      def marks(self,person_marks):
          self.marks=person_marks
      def display(self):
          print(self.name,self.rno,self.age,self.marks)
s=student('Tajinder',123)
s.age(21)
s.marks(99)
s.display()

#ques3
class temprature():
    def fahrenheit(self,c):
        self.celcius=c
        self.fahren=(self.celcius*1.8)+32
        print("temp in fahrenheit is:",self.fahren)
    def cel(self,f):
        self.fahren=f
        self.celcius=(self.fahren-32)*1.8
        print("temp in celcius is:",self.celcius)
t=temprature()
t.fahrenheit(32)
t.cel(100)

#ques4
class movie_detail():
     def add_detail(self,artist,release,rating):
         self.art=artist
         self.rel=release
         self.rate=rating
     def display(self):
         print(self.art,self.rel,self.rate)
m=movie_detail()
m.add_detail('Tajinder',2019,5)
m.display()

#ques5
class Animal():
    def animal_attribute(self,name):
        self.naam=name
        print(self.naam)
class Tiger(Animal):
    def name(self):
        pass
t=Tiger()
t.animal_attribute("Babbar sher")

#ques6
'''
    A B
    A B
'''

#ques7
class shape:
    def area(self):
        self.l=int(input("enter length"))
        self.b=int(input("enter breath"))
class rect(shape):
    def area(self):
        self.l=int(input("enter length"))
        self.b=int(input("enter breath"))
        self.ar=self.l*self.b
        print(self.ar)
class square(shape):
    def area(self):
        self.l=int(input("enter side of square"))
        self.ar=self.l*self.l
        print(self.ar)
x=shape()
y=rect()
z=square()
y.area()
z.area()
                   
    
    

    
