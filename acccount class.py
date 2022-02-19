                                                                                                                                                                                                                                                                        # account class imp concept
#1) design the clASS name account that contains:

#
#- a private id for account
#-a balance for account
#-a private intrate for annual intrest rate
#-a constructor that creates an account with specified id,initial balance and intrest rate
#- a method name GETMONTHLYINTRESTRATE() that returnsmonthly intrest rate
#-a method name CHECKBALANCE() that return balance amount from the account
#-a method name WITHDRAW(N) that withdraws a specified amount from the account
#-a method name DEPOSIT(m) that deposit


class account:
    def __init__(self,i,b,ir):
        self.__id=i
        self.__bal=b
        self.__intrate=ir 

    def __str__(self):
        return(str(self.__id)+','+str(self.__bal)+','+str(self.__intrate))
    def getmonthlyintrate(self):
        return self.__intrate
    def checkbal(self):
        return self.__bal

    def withdraw(self,n):
        self.__bal=self.__bal-n

    def deposit(self,m):
        self.__bal=self.__bal+m
    def accid(self):
        return self.__id


ac=list(range(100,110))
ba=[200,1000,500,4554,10000,345,708965,84847548,123467,987654]

account_list=[]
for i in range(len(ac)):
    account_list.append(account(ac[i],ba[i],4))

for i in account_list:
    print(i)

acc_num=int(input('Enter an account number'))
idx=-1
for i in account_list:
    print(i.accid())
    if i.accid()==acc_num:
        v=1
        idx=idx+1
        break;
    else:
        v=0
        idx=idx+1

if v==1:
    print('valid acount number')
    x=int(input('1.withdraw,2.deposit,3.check balance,4.exit'))
    if x==3:
        print(account_list[idx].checkbal())

else:
    print('Invalid account number')
