
from cryptography.fernet import Fernet

print("Enter the Text which you want to Encrypt")
message = input()



key = Fernet.generate_key()



fernet = Fernet(key)


encMessage = fernet.encrypt(message.encode())

print("original string was : " , message)
print("encrypted string is : " , encMessage)



print("Press Any key to Exit")
stop = input()
