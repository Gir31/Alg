import ex_01_10_2021184002_2 as qs


def selection(arr, start, end, nth):
	pivot = qs.partition(arr, start, end)
	ss = pivot - start

	if ss + 1 == nth:
		return arr[pivot]
	elif ss + 1 > nth:
		return selection(arr, start, pivot - 1, nth)
	elif ss + 1 < nth:
		nth = nth - ss - 1
		return selection(arr, pivot + 1, end, nth)


def main():
	print(qs.words)
	print(qs.partition)

	ranks = [3, 17, 23, 88, 99]

	last_word_index = len(qs.words) - 1
	for rank in ranks:
		words = qs.words[:]
		word = selection(words, 0, last_word_index, rank)
		print(f'{rank=} {word=}')




if __name__ == '__main__':
	main()