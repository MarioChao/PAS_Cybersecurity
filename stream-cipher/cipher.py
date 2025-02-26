def modSlice(text: bytes, start: int = 0, end: int = -1, step: int = 1) -> bytes:
	length = len(text)
	return bytes(text[i % length] for i in range(start, end, step))

def keyGenerator(seed: bytes):
	# Set up generator using seed
	length = yield b""
	array = [
		[b"whatlifeis 1OR 1"[4*i:4*i+4] for i in range(4)],
		[b"==1 overflow sql"[4*i:4*i+4] for i in range(4)],
		[b"dataokayeverletu"[4*i:4*i+4] for i in range(4)],
		[b"go!=#8(2`.cmgone"[4*i:4*i+4] for i in range(4)],
	]
	bigMod = 10**100 + 7
	rowIndex = 1948101946
	colIndex = 22340123
	byteIndex = 8691913
	seed_index = 0
	seed += b"deadbeef"

	# Generator
	while True:
		keystream = b""
		for _ in range(length):
			# 1 round
			for i in range(4):
				for j in range(4):
					# Update array
					array[i][j] = xor_bytes(array[i-3][j-3], array[i][j])
					array[i][j] = xor_bytes(array[i][j], modSlice(seed, seed_index, seed_index+4))
					seed_index = (seed_index + 4) % len(seed)

					# Internal states
					rowIndex = rowIndex * (5 + array[i][j][0]) % bigMod + 999
					colIndex = colIndex * (4 + array[i][j][1]) % bigMod + 888
					byteIndex = byteIndex * (3 + array[i][j][2]) % bigMod + 777
					seed = xor_bytes(seed, array[i][j][::-1])
			# Add key
			keystream += array[rowIndex % 4][colIndex % 4][byteIndex % 4].to_bytes()
		length = yield keystream

def xor_bytes(text: bytes, key: bytes) -> bytes:
	# XOR text by key
	result = b""
	j_index = 0
	for b in text:
		result += (b ^ key[j_index]).to_bytes()
		j_index = (j_index + 1) % len(key)
	return result

def runCipher():
	print("-- Running encrypt cipher --")
	# Get seed
	print("First, give me a seed.")
	print("This will determine the oracle's response.")
	seed = input("Your seed (string): ").encode()
	generator = keyGenerator(seed)
	next(generator)

	# Oracle
	while True:
		# Get message
		message = input("Message to encrypt (string): ")

		# Generate keystream
		keystream = generator.send(len(message))

		# Create ciphertext
		ciphertext_bytes = xor_bytes(message.encode(), keystream)
		print(f"Ciphertext hex: {ciphertext_bytes.hex()}")

def decryptCipher():
	print("-- Running decrypt cipher --")
	# Get seed
	seed = input("Your seed (string): ").encode()
	generator = keyGenerator(seed)
	next(generator)

	# Oracle
	while True:
		# Get message
		message_hex = input("Message to decrypt (hex): ")
		message = bytes.fromhex(message_hex).decode()

		# Generate keystream
		keystream = generator.send(len(message))

		# Create plaintext
		plaintext_bytes = xor_bytes(message.encode(), keystream)
		print(f"Plaintext bytes: {plaintext_bytes}")

def about():
	# Introduction
	print(f"o {"- " * 23:^50}o")
	print("Welcome to the oracle!")
	print("Send me a message and I will encrypt it for you.")
	print()

if __name__ == "__main__":
	# Input mode
	print()
	print("Modes: (0 = encrypt, 1 = decrypt)")
	mode = input("Enter mode: ")
	while not mode in ("0", "1"):
		mode = input("Enter mode: ")
	print()

	# Run mode
	if mode == "0":
		about()
		runCipher()
	else:
		decryptCipher()
