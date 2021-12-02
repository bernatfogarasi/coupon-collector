import math

def probability_of_not_collected(coupons, days):
	'''
	calculate the probability that a
	full set of coupons was NOT collected by a given day
	'''
	pass



def probability_of_collected(coupons, days):
	'''
	calculate the probability that a
	full set of coupons was collected by a given day
	'''
	return 1 - probability_of_not_collected(coupons, days)

def main():
	probability(5, 11)

if __name__ == '__main__':
	main()