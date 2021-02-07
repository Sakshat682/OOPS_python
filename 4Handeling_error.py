try:
  numinator = int(input("Enter the numinator:"))
  denominator = int(input("Enter the denominator: "))
  print(numinator/denominator)
except ValueError:
  print("Entered input is not valid")
except ZeroDivisionError:
  print("Division by zero is not possible, se dividing by 0.001 instead of zero")
  print(numinator/0.001)
except:
  print("Operation was unsucceful")

print("DIVISION ATTEMPTED BY USER")


# numinator = int(input("Enter the numinator:"))
# denominator = int(input("Enter the denominator: "))
# print(numinator/denominator)