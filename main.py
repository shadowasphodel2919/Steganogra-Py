import cv2
input_image = cv2.imread('test.png')

# Resize the image to required size
input_image = cv2.resize(input_image, (512, 512))

message = 'General Kenobi'+'%'

bin_message = ''.join(format(ord(i), '08b') for i in message)
N = len(bin_message)

output_image = input_image.copy()
count = 0

for i in range(len(input_image)):
    for j in range(len(input_image[0])):
        if(count<N):
            for k in range(len(input_image[i][j])):
                LSB = input_image[i][j][k]&1
                if(LSB != int(bin_message[min(count, N - 1)])):
                    output_image[i][j][k] = (input_image[i][j][k]  & ~1) | int(bin_message[min(count, N - 1)])
                
                # print(LSB, bin_message[min(count, N-1)], output_image[i][j][k]&1, output_image[i][j][k], input_image[i][j][k])
                count += 1

cv2.imwrite("output.png", output_image)
