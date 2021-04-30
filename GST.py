#Find GST Using Python
#by @programmers0_0

op = int(input("Enter Original Price:")) #op meanse Original Price
GST = int(input("Enter GST:")) # Get GST from User

cal = op*GST/100

total = op + cal

print("Total Amount:",total)