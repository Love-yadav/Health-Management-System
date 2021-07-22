#Health Managment System
#3 clients:-Harry Rohan anid Hamad
# # total 6 files
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# write a function that when Executed takes as input client name
#write one more function that retrived the food or exercise for the choosen nam_
def get_date():
    import datetime
    return datetime.datetime.now()

def log(option1,option2,option3):

    if option1==1 and option2==1 and option3==1:
        with open("Harry_Diet.txt","a")as Ha:
         Ha.write(str(get_date())+":- "+input("enter the food consume by  you:")+"\n")
         print("your food is added successfully")
    
    if option1==1 and option2==2 and option3==1:
        with open("Rohan_Diet.txt","a")as Ro:
         Ro.write(str(get_date())+":- "+input("enter the food consume by  you:")+"\n")
         print("your food is added successfully")

    if option1==1 and option2==3 and option3==1:
        with open("Hammad_Diet.txt","a")as Hamm:
         Hamm.write(str(get_date())+":- "+input("enter the food consume by  you:")+"\n")
         print("your food is added successfully")

#form here the Exercise section is started
    if option1==1 and option2==1 and option3==2:
        with open("Harry_Exercise.txt","a")as Ha:
         Ha.write(str(get_date())+":- "+input("enter the Exercise done by  you:")+"\n")
         print("your Exercise is added successfully")

    if option1==1 and option2==2 and option3==2:
        with open("Rohan_Excercise.txt","a")as Ro:
         Ro.write(str(get_date())+":- "+input("enter the Exercise done by  you:")+"\n")
         print("your excercise is added successfully")
    
    if option1==1 and option2==3 and option3==2:
        with open("Hammad_Excercise.txt","a")as Hamm:
         Hamm.write(str(get_date())+":- "+input("enter the Excercise done by  you:")+"\n")
         print("your excercise is added successfully")
    else:
        print("--------------Please choose form the option-------------------------------")
        print("----------------------try again----------------------------------")
    
#what if when someone wants to retrive their data
#retrive data for food starts here
def retrive(option1,option2,option3):
    if option1==2 and option2==1 and option3==1:
        with open("Harry_Diet.txt")as Ha:
            result=Ha.read()
            print(result)
    if option1==2 and option2==2 and option3==1:
        with open("Rohan_Diet.txt")as Ha:
            result=Ha.read()
            print(result)
    if option1==2 and option2==3 and option3==1:
        with open("Hammad_Diet.txt")as Ha:
            result=Ha.read()
            print(result)
#retrive data of the excercise start here
    if option1==2 and option2==1 and option3==2:
        with open("Harry_Exercise.txt")as Ha:
            result=Ha.read()
            print(result)
    if option1==2 and option2==2 and option3==2:
        with open("Rohan_Excercise.txt")as Ha:
            result=Ha.read()
            print(result)
    if option1==2 and option2==3 and option3==2:
        with open("Hammad_Excercise.txt")as Ha:
            result=Ha.read()
            print(result)
    else:
        print("you choose invalid options ")
        print("try again later")

if __name__=='__main__':
    print("-----------------------welcome to The Health Managment System------------------------------")
    print("--------------------what do you want to do--------------------------")
    print("1.Log the input")
    print("2.Retrive the input")
    option1=int(input("enter your choice:"))

    print("-----------------------Select an option---------------------------------------")
    print('1.Harry')
    print("2.Rohan")
    print("3.Hammad")
    option2=int(input("Enter your choice:"))
    print("------------------------what do you see about the selected name----------------------")
    print("--------------select an option---------------------")
    print("1.Diet")
    print("2.Exercise")
    option3=int(input("enter your choice:"))
    # food=input("enter the food which is consume by you:")
    log(option1,option2,option3)
    retrive(option1,option2,option3)
    
    
    