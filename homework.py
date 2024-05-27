#ask the user to input their age
Age = int(input ("Enter your age:"))
#Ask the user to input whether they are a student or not (input 'yes' if theyare a student, 'no' otherwise).
student = input ("Are you a student?(yes/no):")
#Use logical operators to determine if the person is eligible for a discount based on the following criteria:
if (Age <= 12) or ( Age>= 13 and Age<=18 and student == 'yes') :
    print ("you are eligible for a discount on a movie ticket ")
else:
    print ("you are not eligible for a discount on the movie ticket")
