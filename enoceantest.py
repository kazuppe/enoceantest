import serial
ser = serial.Serial('/dev/tty.usbserial-FT2LMD98',57600,timeout=1)
while True:
  try:
    c = ser.read()
    if c != b'U':
        continue
    else:
        clist = [85]
        c = ser.read(15)
        [clist.append(i) for i in c]
        print(clist)
  except KeyboardInterrupt:
    ser.flush()
    ser.close()
    exit()
