# settings.py

ENERGY_PER_FLOP = 5e-3  # Example: 5 millijoules per FLOP...
UTILIZATION_THRESHOLD = 0.9  # Only use up to 80% of node capacity
FLOPS = [1.58*10**3, 2.49*10**3, 3.09*10**3, 5.62*10**3, 4.16*10**3, 5.35*10**3, 5.65*10**3, 8.12*10**3, 4.98*10**3, 6.06*10**3, 6.69*10**3, 8.87*10**3, 11.34*10**3, 10.97*10**3, 12.15*10**3, 10.07*10**3, 13.45*10**3, 16.31*10**3, 29.80*10**3, 35.60*10**3, 20.14*10**3, 26.90*10**3, 32.62*10**3, 29.80*10**3, 35.60*10**3]  #TFLOPS 
FLOPS_WATT = [6.48, 6.82, 15.85, 18.73, 16.62, 21.38, 22.58, 21.66, 30.19, 24.24, 26.76, 49.29, 45.36, 43.88, 48.60, 46.84, 53.80, 82.26, 93.13, 101.71, 93.67, 107.60, 116.50, 93.13, 101.71] #GFLOPS/watt


MIN_REQUIRED_ACCURACY = 0.3
MAX_REQUIRED_ACCURACY = 0.95
MIN_RESPONSE_TIME = 1.5 # second
MAX_RESPONSE_TIME = 4.0
TIME_SLOT = 10
NUM_REQUEST = 10