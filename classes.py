class Laptop:

    ram = '8 gb'
    brand = 'Asus'
    hdd = '1 tb'
    resolution = '1080p'

    def playGame(self):
        print('Laptop plays games')
       
    def playVideo(self):
        print('Laptop plays videos')


lappy = Laptop()

lappy.playGame()
lappy.playVideo()

print(lappy.resolution)

class Account:

    def __init__(self, name, acc_no, branch, balance):

        self.holder_name = name
        self.acc_no = acc_no
        self.branch = branch
        self.balance = balance

    def debit(self, amt):
        self.balance = amt
        print(f"{amt} debited from {self.holder_name}'s account")
    def playGame(self):
        print('Laptop plays games')


acc1 = Account("Mr. Neo Anderson", 123456789, 'hazratganj', 2000)
acc2 = Account("Mrs. Neo Anderson", 987654321, 'hazratganj', 5000)

acc1.debit(1500)
acc2.debit(2300)

print(acc1.balance)
print(acc2.balance)
 

