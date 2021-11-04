import random
from pprint import pprint
import time

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
		if len(collections) % (len(collections) / 100) == 0:
			portion = len(collections) / collection_count
			time_taken = time.time() - start_time
			eta = calculate_eta(portion, time_taken)
			percentage = portion * 100
			eta_seconds = eta % 60
			eta_minutes = ((eta - eta_seconds) / 60) % 60
			eta_hours = (eta - eta_seconds - eta_minutes) / 3600
			print(f"PROCESSING progress={percentage:.2f}% time={time_taken} eta={str(int(eta_hours)).zfill(2)}:{str(int(eta_minutes)).zfill(2)}:{str(int(eta_seconds)).zfill(2)}")
	return collections

def main():
	collections = create_collections(10000)
	with open("data.txt", "w") as file:
		file.write("\n".join(["\t".join(str(item) for item in collection) for collection in collections]))
	
if __name__ == '__main__':
	main()