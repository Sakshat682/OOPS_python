while True:

  try:
    num = int(input("Enter a number: "))
    print(f"you entered {num}")
    break
  
  except:
    print("Invalid Input")
  
  # print("ATTEMPTED INPUT")
  finally:
    print("ATTEMPTED INPUT")

# def hello():
#   try:
#     num = int(input("Enter the number"))
#     return 5   
#   except:
#     print("not a valid number")
#   finally:
#     print("HI IT IS FINALLY BLOCK")


# print(hello())