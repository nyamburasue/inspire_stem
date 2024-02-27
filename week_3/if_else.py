#program to test on if or else
#name : Susan Maina
#date :26/02/2024

age = 17

if age > 18.1 :
    print ("you are allowed to drive")

# finding 0.1 increment
    
salary = 45000
if salary > 30000 and salary < 50000 :
    salary = salary * 0.1 + salary 
    print (salary)

home_county = "nyeri"
if home_county == "nyeri" or home_county == "kisii" :
    print ("you win a bursary")

grade = 70

if grade >= 84 and grade <= 90 :
    print ("you win a calculator")
elif grade >= 50 and grade <= 83 :
    print ("you win a mathematicals set")
else :
    print ("you win nothing")