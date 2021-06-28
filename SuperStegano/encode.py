from index import create_image

message = input("Enter the message to encode=>  ")
source = input("Enter the file name you want to Encode?=>  ")
destination = input("Enter the output file name?(.png extension only)=>  ")

create_image(message, source, destination)