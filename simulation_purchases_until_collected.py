import random
from pprint import pprint
import time
import matplotlib.pyplot as plt
import numpy

def calculate_multiplied_harmonic_series(n):
	series = [1]
	temp = [1]
	for i in range(1, n):
		temp_new = temp[i - 1] + 1 / (i + 1)
		temp.append(temp_new)
		series.append(i * temp_new)
	return series

def calculate_eta(portion, time):
	return time / portion - time

def create_collection(coupon_count):
	collection = {
		"coupon_count": coupon_count,
		"sequence": []
	}
	i = 0
	while True:
		i += 1
		collection["sequence"].append(random.randint(1, coupon_count))
		if len(set(collection["sequence"])) == collection["coupon_count"]:
			collection["collected_after"] = i
			break
	return [collection["coupon_count"], collection["collected_after"]]

def create_collections(collection_count):
	start_time = time.time()
	collections = []
	for _ in range(collection_count):
		collections.append(create_collection(random.randint(1, 1000)))
		if len(collections) % (len(collections) / collection_count) == 0:
			portion = len(collections) / collection_count
			time_taken = time.time() - start_time
			eta = calculate_eta(portion, time_taken)
			percentage = portion * 100
			eta_seconds = eta % 60
			eta_minutes = ((eta - eta_seconds) / 60) % 60
			eta_hours = (eta - eta_seconds - eta_minutes) / 3600
			print(f"PROCESSING progress={percentage:.2f}% time={time_taken} eta={str(int(eta_hours)).zfill(2)}:{str(int(eta_minutes)).zfill(2)}:{str(int(eta_seconds)).zfill(2)}")
	return collections

def plot(collections):
	font = {'size': 14}
	x = [collection[0] for collection in collections]
	y = [collection[1] for collection in collections]
	
	plt.xlabel("Unique coupons", fontdict=font)
	plt.ylabel("Purchases until full set", fontdict=font)
	plt.scatter(x, y, marker=".", color="black", alpha=0.02)
	plt.plot(numpy.arange(1, 1001), calculate_multiplied_harmonic_series(1000), color="black")
	plt.legend(["Expected", "Simulation"], loc=4)
	# plt.yscale("log")
	plt.show()

def main():
	# collections = create_collections(10000)
	# with open("data.txt", "w") as file:
	# 	file.write("\n".join(["\t".join(str(item) for item in collection) for collection in collections]))
	with open("data.txt", "r") as file:
		collections = [[int(item) for item in collection.strip().split()] for collection in file.readlines()]
	print(collections)
	plot(collections)

	
if __name__ == '__main__':
	main()