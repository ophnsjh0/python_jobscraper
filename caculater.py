def plus(a=0, b=0):
      int(a)
  int(b)
  print(a + b)


def minus(a=0, b=0):
  int(a)
  int(b)
  print(a - b)


def multi(a=0, b=0):
  int(a)
  int(b)
  print(a * b)


def div(a=0, b=0):
  int(a)
  int(b)
  print(a / b)


def exp(a=0, b=0):
  int(a)
  int(b)
  print(a)


def main():
  value1 = int(input("첫 값"))
  value2 = int(input("두번째 값"))
  oper = input("연산기호 입력")
  if oper == "+":
    plus(value1, value2)
  elif oper == "-":
    minus(value1, value2)
  elif oper == "*":
    multi(value1, value2)
  elif oper == "/":
    div(value1, value2)
  elif oper == "**":
    exp(value1, value2)
  else:
    print("연산 기호를 잘못 입력하였습니다. 다시 시도해 주세요")


main()
