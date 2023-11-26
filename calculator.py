# match case


num1 = int(input("enter your num1: "))
num2 = int(input("enter your num2: "))
operator = input("enter your operator : ")

match operator:
    case "+":
        print("sum is :", num1 + num2)

    case "-":
        print("the diff is :", num1-num2)

    case " * ":
        print(" Multiplication is :", num1 * num2)
