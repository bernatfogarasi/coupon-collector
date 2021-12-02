import pandas
import matplotlib.pyplot as plt
import numpy
import sympy
# plt.style.use("grayscale")
plt.rcParams.update({'font.size': 16})


def calculate_reciprocals(n):
	return [1/i for i in range(1, n + 1)]

def calculate_harmonic_series(n):
	series = [1]
	for i in range(1, n):
		series.append(series[i - 1] + 1 / (i + 1))
	return series

def calculate_logarithmic_series(n):
	return [numpy.log(i) for i in range(1, n + 1)]

def calculate_euler_mascheroni_constant():
	from sympy.abc import k
	x = sympy.symbols('x')
	return sympy.limit(sympy.Sum(1 / k, (k, 1, x)).doit() - sympy.ln(x), x, numpy.Infinity)

def main():
	font = {'size': 20}
	# reciprocals = calculate_reciprocals(LENGTH)
	LENGTH = 5
	harmonic_series = calculate_harmonic_series(LENGTH)
	natural_logarithm = calculate_logarithmic_series(LENGTH)
	estimates = numpy.add(natural_logarithm, sympy.EulerGamma.evalf())
	estimates = numpy.add(estimates, [1/2/(i+1) for i in range(1, LENGTH + 1)])
	estimate_error = numpy.subtract(harmonic_series, estimates)
	x = numpy.arange(1, LENGTH + 1)

	# fig, ax = plt.subplots(nrows=1)
	# ax.set_axisbelow(True)
	# ax.plot(x, harmonic_series, marker=".", color="black")
	# ax.set_xlabel("n", fontdict=font)
	# ax.legend([r"$H_n$"], loc=4)
	# plt.tight_layout()
	# plt.show()
	# return
	fig, ax = plt.subplots(nrows=2, ncols=2)
	ax[1, 0].set_xlabel("n", fontdict=font)
	# ax[0, 0].grid()
	# ax[1, 0].grid()
	ax[0, 0].plot(x, harmonic_series, marker=".", color="black")
	ax[0, 0].plot(x, estimates, marker=".", color="grey", alpha=0.5)
	ax[1, 0].plot(x, estimate_error, marker=".", color="black")
	ax[0, 0].legend([r"$H_n$", r"$\ln{n}+\gamma+\frac{1}{2n}$"], loc=4)
	ax[1, 0].legend([r"Approximation error"], loc=1)
	ax[0, 0].set_xlim([0, LENGTH])
	ax[1, 0].set_xlim([0, LENGTH])
	ax[1, 0].set_yscale("log")
	ax[0, 0].xaxis.set_ticklabels([])



	LENGTH = 50
	harmonic_series = calculate_harmonic_series(LENGTH)
	natural_logarithm = calculate_logarithmic_series(LENGTH)
	estimates = numpy.add(natural_logarithm, sympy.EulerGamma.evalf())
	estimates = numpy.add(estimates, [1/2/(i+1) for i in range(1, LENGTH + 1)])
	estimate_error = numpy.subtract(harmonic_series, estimates)
	x = numpy.arange(1, LENGTH + 1)

	# ax[0, 1].grid()
	# ax[1, 1].grid()
	ax[0, 1].plot(x, harmonic_series, marker=".", color="black")
	ax[0, 1].plot(x, estimates, marker=".", color="grey", alpha=0.5)
	ax[1, 1].plot(x, estimate_error, marker=".", color="black")
	ax[0, 1].set_xlim([0, LENGTH])
	ax[1, 1].set_xlim([0, LENGTH])
	ax[1, 1].set_yscale("log")
	ax[0, 1].xaxis.set_ticklabels([])
	# plt.tight_layout()
	plt.show()

	# plt.show()

if __name__ == '__main__':
	main()