import matplotlib.pyplot as plt


restarts_diag = [85, 317, 602]
restarts_tree = [388, 933, 2090]

tau_diag = [(85 / 2**11), (317 / 2**12), (602 / 2**13)]
tau_tree = [(388 / 2**11), (933 / 2**12), (2090 / 2**13)]

time_diag = [193, 397, 831]
time_tree = [246, 502, 1060]

tuning_round = [11, 12, 13]

plt.figure(figsize=(10, 6))
plt.plot(time_diag, restarts_diag, label='diag')
plt.plot(time_tree, restarts_tree, label='tree')
plt.legend()
plt.title('num restarts vs time plot')
plt.xlabel('time (seconds)')
plt.ylabel('num restarts')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(tuning_round, restarts_diag, label='diag')
plt.plot(tuning_round, restarts_tree, label='tree')
plt.legend()
plt.title('num restarts vs tuning round plot')
plt.xlabel('tuning round (r)')
plt.ylabel('num restarts')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(tuning_round, tau_diag, label='diag')
plt.plot(tuning_round, tau_tree, label='tree')
plt.legend()
plt.title('restart rate vs tuning round plot')
plt.xlabel('tuning round (r)')
plt.ylabel('restart rate')
plt.grid(True)
plt.show()

gcb_diag = [3.1, 3.39, 3.37]
gcb_tree = [1.14, 0.951, 0.763]

plt.figure(figsize=(10, 6))
plt.plot(tuning_round, gcb_diag, label='diag')
plt.plot(tuning_round, gcb_tree, label='tree')
plt.legend()
plt.title('GCB vs tuning round plot')
plt.xlabel('tuning round (r)')
plt.ylabel('GCB')
plt.grid(True)
plt.show()