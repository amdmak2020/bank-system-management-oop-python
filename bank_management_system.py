class Everybody():
    def __init__(self, first_name, last_name, pw, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.pw = pw
        self.age = age
        self.sex = sex

class Customers(Everybody):
    def __init__(self, first_name, last_name, pw, age, sex, balance):
        super().__init__(first_name, last_name, pw, age, sex)

        self.balance = balance
    @property
    def email(self):
        return "{}.{}.cust@gmail.com".format(self.first_name, self.last_name)
    @property
    def put_or_take_money(self):
        return "{} $".format(self.balance)
    @put_or_take_money.setter
    def put_or_take_money(self, value):
        self.balance = self.balance + value
    

class Employee(Everybody):
    def __init__(self, first_name, last_name, pw, age, sex, postition, salary):
        super().__init__(first_name, last_name, pw, age, sex)
        self.postition = postition
        self.salary = salary
        self.salary = "{} $".format(self.salary)
    @property
    def email(self):
        return "{}.{}.empl@gmail.com".format(self.first_name, self.last_name)


x = Customers("born2", "die", "post malone is lit af", 18, "male",0)
y = Employee("xxx", "tentacion", "post malone is still lit af", 45, "male", "accountant", 2500)

print(x.put_or_take_money)

x.put_or_take_money = 2000

print(x.put_or_take_money)


