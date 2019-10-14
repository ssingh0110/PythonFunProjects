print("#---RGB to HEX Converter---#")
print("Range of Inputs: 0-255")
while(1):
    R = int(input("R:"))
    G = int(input("G:"))
    B = int(input("B:"))
    if R > 255 or R < 0 or G < 0 or G > 255 or G < 0 or B > 255:
        print("Bad Inputs Provided!!")
    else:
        hex_R, hex_G, hex_B = hex(R).split("x"), hex(G).split("x"), hex(B).split("x")
        if len(hex_R[-1])==1:
            hex_R = '0'+hex_R[-1]
        else:
            hex_R = hex_R[-1]
        if len(hex_G[-1])==1:
            hex_G = '0'+hex_G[-1]
        else:
            hex_G = hex_G[-1]
        if len(hex_B[-1])==1:
            hex_B = '0'+hex_B[-1]
        else:
            hex_B = hex_B[-1]
        print("Hex: #%s"%(hex_R+hex_G+hex_B).upper())
        try:
            if(int(input("Press 1 to exit \n")))==1:
                break
        except ValueError:
            pass