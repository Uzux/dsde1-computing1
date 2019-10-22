import math as m

def main():
    while True:
        user_input = input("Input the length of the pendulum in meters:")
        try:
            val = int(user_input)
            break
        except ValueError:
            print("That's not an int")

    while True:
        user_input = input("Input the acceleration of the system:")
        try:
            dyspeed = int(user_input)
        except ValueError:
            print("That's not an int")


    length = val
    accel = dyspeed
    perio = period(length, accel)
    print(perio)

def period(length, accel):
    if accel != 0:
        t = 2*m.pi*m.sqrt(length/accel)
        return t
    else:
        print("Acceleration cannot be 0!")
        raise ValueError
if __name__ == '__main__':
    main()