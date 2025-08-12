import qrcode

print("Welcome to the QR Code Generator!")

url = input("Please enter the URL you want to encode in a QR code: ")
name = input("Please enter the file name: ")

fileName = name + ".png"

img =  qrcode.make(url)

print("Your url: ", url)


img.save(fileName)
print(f"QR code generated and saved as {fileName}")

