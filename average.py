def sum ():
    number_of_subject = int(input("Enter number of subject: "))
    sum = 0
    for i in range(1 , number_of_subject+1):
        grade = int(input(f"Enter a {i}th grade: "))
        sum += grade
    return sum , number_of_subject
def average (x , y):
    return f"your average is {x/y}"
sum_ , count = sum()
print(average(sum_ , count))