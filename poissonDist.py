import scipy.stats as st

# Inputs
lambda_val = float(input("Enter the population average rate (lambda): "))
observed = int(input("Enter the observed count: "))

# Determine the expected (mean) count
expected = lambda_val

# If observed < expected, sum both tails:
if observed < expected:
    lower_tail = st.poisson.cdf(observed, lambda_val)
    upper_tail = st.poisson.sf(2 * expected - observed - 1, lambda_val)
else:
    upper_tail = st.poisson.sf(observed - 1, lambda_val)
    lower_tail = st.poisson.cdf(2 * expected - observed, lambda_val)

# Two-tailed probability
p_value = lower_tail + upper_tail

print(f"The two-tailed probability of observing a count as extreme as {observed} is {p_value:.6f}.")
