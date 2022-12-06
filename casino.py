# from random import randint

# def casino():
#   user_num = int(input("num :"))
#   cpu_num = randint(1, 50)
#   while user_num != cpu_num:
#     print("Sorry, you not correct")
#     if user_num <= cpu_num:
#       print("Lower, Continue", cpu_num)
#       user_num = int(input("num :"))
#     elif user_num >= cpu_num:
#       print("Higer, Continue", cpu_num)
#       user_num = int(input("num :"))

#     if user_num == cpu_num:
#       print("Good, Conguratulation", cpu_num)

# casino()

from random import randint


def casino():
    print("welcome to Python Casino")
    playing = True
    cpu_num = randint(1, 50)

    while playing:
        user_num = int(input("Choose num :"))
        print("Sorry, you not correct")
        if user_num == cpu_num:
            print("Good, Conguratulation", cpu_num)
            playing = False
        elif user_num <= cpu_num:
            print("Lower, Continue", cpu_num)
        elif user_num >= cpu_num:
            print("Higer, Continue", cpu_num)


casino()
