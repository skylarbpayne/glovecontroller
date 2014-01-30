import serial

ser = serial.Serial(5, 9600)
ser.timeout = None

while True:
    ser.write(bytes(1))
    
    inputs = ser.read(6)

    for i in range(0, len(inputs)):
        print("A" + str(i) + ": " + str(inputs[i]))
    print("\n")
