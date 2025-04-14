from secret import flag1, flag2, flag3
from Crypto.Util.number import bytes_to_long
from random import randint


def get_number():
	num = float(input("> "))
	return num


def verify_quiz():
	print("Enter a number")
	num1 = get_number()
	print(f"base number = {num1}")

	print("Enter an addend")
	num2 = get_number()
	print(f"{num1}+{num2} = {num1 + num2}")

	print("Enter a subtrahend")
	num2 = get_number()
	print(f"{num1}-{num2} = {num1 - num2}")

	print("Enter a multiplicand")
	num2 = get_number()
	print(f"{num1}*{num2} = {num1 * num2}")

	print("Enter a divisor")
	num2 = get_number()
	print(f"{num1}/{num2} = {num1 / num2}")

	print("Enter an exponent")
	num2 = get_number()
	print(f"{num1}^{num2} = {num1 ** num2}")


def clear_sky():
	print("Meanwhile, here's a pastime riddle.")
	print()
	print("I'm an idol on the internet. I love to sing, especially in Japanese. I live in a software.")
	print("Who am I? (two words, capitalized)")
	print("When you're ready for the game, enter \"let's go\" to proceed")
	while True:
		question_str = input("> ")
		question_long = bytes_to_long(question_str.encode())
		if question_long == 22400736435988857272861813621:
			print("Wow, how did you know my secret?")
			print(flag2)
		elif question_long == 7810776841528043375:
			break
		else:
			continue


def red_light_green_light():
	tiles = 100
	rounds = 32
	light_limit_range = (2, 5)

	current_position = 0
	print(f"There are {tiles} tiles, and there's {rounds} rounds of movement.")
	print(f"Each green light, you can move up to {light_limit_range} tiles, which is selected by random each round.")
	print()
	input("Enter to proceed")
	print()

	for i in range(rounds):
		if not (current_position < tiles):
			break

		print(f"#.#.# Round {i + 1} / {rounds} #.#.#")
		print(f"Your progress is {current_position}/{tiles}.")
		print()

		print("#.# Green light! #.#")
		print("How many tiles to move?")
		tiles_to_move = get_number()
		print()

		print("#.# Red light! #.#")
		light_limit = randint(light_limit_range[0], light_limit_range[1])
		if tiles_to_move > light_limit:
			print("You moved on red!")
			break

		print(f"Moving by {tiles_to_move}")
		current_position += tiles_to_move

	print()
	print("#.#.# Result #.#.#")
	print(f"{current_position}/{tiles}")
	print()

	if current_position >= tiles:
		print("You win! Congratulations!")
	elif current_position < tiles:
		print("You failed to reach the end. Eliminated!")
	else:
		print("How did you get there?")
		print(flag3)


def main_loop():
	print("---------- Pas no Uta ----------")
	print("To verify, respond to the following questions.")
	print()
	verify_quiz()
	print("You are now verified!")
	print()

	print("*+*+*+* Clear Sky *+*+*+*")
	print("Welcome to the atrium.")
	print("We will be starting the red light green light game shortly.")
	print()
	clear_sky()
	print()

	print("#.#.#.#.# Red Light, Green Light #.#.#.#.#")
	print("This game is straightforward.")
	print("Move when it's green.")
	print("No movements on red.")
	print()
	red_light_green_light()
	print()

	print("That's it; this is the end of the program.")


try:
	main_loop()
except Exception as e:
	if isinstance(e, ValueError):
		print("Invalid value (value error)!")
		exit()
	if isinstance(e, ZeroDivisionError):
		print("It's a division by zero!")
		exit()
	if isinstance(e, ArithmeticError):
		print("You broke math! Here's your reward.")
		print(flag1)
		exit()

	# Other exceptions
	print(f"{type(e).__name__}: {e}")
