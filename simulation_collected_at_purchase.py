import random
from pprint import pprint
import time
import matplotlib.pyplot as plt
import numpy
from collections import Counter

def calculate_eta(portion, time):
	return time / portion - time

def create_sample(max_purchase_count, coupon_count):
	purchase_count = random.randint(1, max_purchase_count)
	coupons = [random.randint(1, coupon_count) for _ in range(purchase_count)]
	return [purchase_count , len(set(coupons))]

def create_samples(sample_count, max_purchase_count, coupon_count):
	start_time = time.time()
	samples = []
	for _ in range(sample_count):
		samples.append(create_sample(max_purchase_count, coupon_count))
		if len(samples) % (len(samples) / sample_count) == 0:
			portion = len(samples) / sample_count
			time_taken = time.time() - start_time
			eta = calculate_eta(portion, time_taken)
			percentage = portion * 100
			eta_seconds = eta % 60
			eta_minutes = ((eta - eta_seconds) / 60) % 60
			eta_hours = (eta - eta_seconds - eta_minutes) / 3600
			print(f"PROCESSING progress={percentage:.2f}% time={time_taken} eta={str(int(eta_hours)).zfill(2)}:{str(int(eta_minutes)).zfill(2)}:{str(int(eta_seconds)).zfill(2)}")
	return samples

def plot(samples):
	font = {'size': 14}
	x = [sample[0] for sample in samples]
	y = [sample[1] for sample in samples]
	
	plt.xlabel("Unique coupons", fontdict=font)
	plt.ylabel("Purchases until full set", fontdict=font)
	plt.scatter(x, y, marker=".", color="black" , alpha=0.02)
	plt.plot(numpy.arange(1, 201), calculate_multiplied_harmonic_series(200), color="black")
	plt.legend(["Expected", "Simulation"], loc=4)
	# plt.yscale("log")
	plt.show()

def main():
	samples1 = create_samples(100000, 100, 10)
	# samples2 = create_samples(10000, 200, 20)

	# print(samples)
	font = {'size': 14}

	# counts = Counter(samples)
	# print(*counts.keys(), sep="\t")
	# print(*counts.values(), sep="\t")
	# plt.hist(samples, COUPON_COUNT, range=[0, COUPON_COUNT])
	# plt.xlim(0, 100)
	plt.xlabel("Purchases", fontdict=font)
	plt.ylabel("Unique coupons collected", fontdict=font)
	plt.scatter([sample[0] for sample in samples1], [sample[1] for sample in samples1], color="black", marker=".", alpha=0.002)
	plt.legend(["Simulation"], loc=4)
	# plt.scatter([sample[0] for sample in samples2], [sample[1] for sample in samples2], color="red", marker=".", alpha=0.02)
	# plt.scatter([sample[0] for sample in samples3], [sample[1] for sample in samples3], color="green", marker=".", alpha=0.02)
	# plt.scatter([sample[0] for sample in samples4], [sample[1] for sample in samples4], color="blue", marker=".", alpha=0.02)
	plt.show()
	# with open("data.txt", "w") as file:
	# 	file.write("\n".join(["\t".join(str(item) for item in sample) for sample in samples]))
	# plot(samples)

	
if __name__ == '__main__':
	main()