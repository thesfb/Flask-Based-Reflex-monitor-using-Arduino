import serial  
import time


def get_reaction(port):
    ser = serial.Serial(port)
    time.sleep(1)

    toggle = True
    lst = []

    while toggle==True:
        for i in range(7):
            rawData = ser.readline().decode('utf')
            print(rawData) 
            lst.append(rawData)  

        op = input("Do you want to exit(Y/n): ")
        if op=='y':
            toggle = False
            ser.setDTR(False)
            time.sleep(1)
            ser.setDTR(True)
            ser.close()
        else:
            lst.clear()
            lst.append('')

    r_time = float(lst[5])
    return r_time


