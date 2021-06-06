def ramanujan(num):
	cache = {}
	twice = {}
	a = 0
	while len(twice) < num:
		a += 1
		b = 0
		while b < a:
			b += 1
			n = a ** 3 + b ** 3

			if n in cache:
				twice[n] = [cache[n], [a, b]]
			else:
				cache[n] = [a, b]

	for n in twice:
		print(n, twice[n])


def ilas_input():

	while True:
		try:
			num = int(
				input("Числа Рамануджана. Введите кол-во чисел для вывода: "))

		except ValueError:
			print("Это не число, попробуйте снова...")

		else:
			ramanujan(num)
			break

ilas_input()

