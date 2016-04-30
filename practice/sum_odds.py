def sum_odds(n):
	count, total = 1, 0
	while count < n:
		if count % 2 != 0:
			total += count
		count += 1
	return total