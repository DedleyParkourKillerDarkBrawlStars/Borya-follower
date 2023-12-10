while True:
    def Test (A, B):
        return A-B
    def TestTwo (A, B):
        return A+B
    def TestThree (A, B):
        return A*B
    def TestFourth (A, B):
        return A/B
    Number = int(input("Введите число"))
    NumberTwo = int(input('Введите втрое число'))
    Option = input('Введите знак')
    if Option == "+":
        print(TestTwo(Number,NumberTwo))
    elif Option == "-":
        print(Test(Number,NumberTwo))
    elif Option == "*":
        print(TestThree(Number,NumberTwo))
    elif Option == "/":
        print(TestFourth(Number,NumberTwo))
    elif Option == "Stop":
        exit()