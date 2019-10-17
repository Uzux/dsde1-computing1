import math as m

def main():
    while True:
        user_input = input("Input the length of the pendulum:")
        type_check = isinstance(user_input, int)
        print (type_check)
        if type_check == True:
            break

    length = int(user_input)
    accel = int(9.81)
    perio = period(length, accel)
    print(perio)

def period(length, accel):
    t = 2*m.pi*m.sqrt(length/accel)
    return t

if __name__ == '__main__':
    main()