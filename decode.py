import cv2

input_image = cv2.imread('output.png', cv2.IMREAD_UNCHANGED) #cv2.IMREAD_UNCHANGED is to extract alpha channelwhich is usually 255 

bin_message = ""
octal = []
c = 0
temp = ""
for i in range(len(input_image)):
    for j in range(len(input_image[0])):
        for k in range(len(input_image[i][j])):
            c += 1
            if(c==8):
                c = 0
                octal.append(temp)
                temp = ""
            LSB = input_image[i][j][k]&1
            bin_message += str(LSB)
            temp += str(LSB)
message = ""
for i in range(0, len(bin_message), 8):
    byte = bin_message[i:i+8]
    if(chr(int(byte,2)) == '%'):
        break
    else:
        message += chr(int(byte,2))
        j += 1
print(message)


