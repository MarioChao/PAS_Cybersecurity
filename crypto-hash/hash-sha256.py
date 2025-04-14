import hashlib

def get_sha256(message: str):
	hashed = hashlib.sha256(message.encode()).hexdigest()
	return hashed

message = input("Enter message: ")
print(get_sha256(message))
