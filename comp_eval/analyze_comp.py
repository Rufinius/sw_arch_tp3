import csv
import numpy as np
import matplotlib.pyplot as plt

metrics2 = []
metrics5 = []
metrics8 = []
res2 = []
res5 = []
res8 = []
eth_metrics2 = []
eth_metrics5 = []
eth_metrics8 = []
eth_res2 = []
eth_res5 = []
eth_res8 = []

data = [metrics2, metrics5, metrics8, res2, res5, res8,
        eth_metrics2, eth_metrics5, eth_metrics8, eth_res2, eth_res5, eth_res8]

files = ['metrics2.csv', 'metrics5.csv', 'metrics8.csv',
         'resource-metrics2.csv', 'resource-metrics5.csv', 'resource-metrics8.csv',
         'eth_metrics2.csv', 'eth_metrics5.csv', 'eth_metrics8.csv',
         'eth_resource-metrics2.csv', 'eth_resource-metrics5.csv', 'eth_resource-metrics8.csv']


for i in range(12):
    with open(files[i]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data[i].append(row)
    data[i] = np.array(data[i])

metrics2 = np.array(metrics2)
metrics5 = np.array(metrics5)
metrics8 = np.array(metrics8)
res2 = np.array(res2)
res5 = np.array(res5)
res8 = np.array(res8)
eth_metrics2 = np.array(eth_metrics2)
eth_metrics5 = np.array(eth_metrics5)
eth_metrics8 = np.array(eth_metrics8)
eth_res2 = np.array(eth_res2)
eth_res5 = np.array(eth_res5)
eth_res8 = np.array(eth_res8)


''' latency plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 5]))), '--', label='Avg. latency for data size 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, metrics5[1::, 5]))), '--', label='Avg. latency for data size 5')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, metrics8[1::, 5]))), '--', label='Avg. latency for data size 8')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Latency in ms')
ax2.set_ylabel('# of users')
ax1.set_title('Avg. Latency comparison')
plt.savefig('Avg. Latency comparison.svg')


''' avg cpu util plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res2[1:61:, 2]))), '--', label='Avg. CPU use for data size 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 2]))), '--', label='Avg. CPU use for data size 5')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res8[1:61:, 2]))), '--', label='Avg. CPU use for data size 8')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('CPU use in %')
ax2.set_ylabel('# of users')
ax1.set_title('Avg. CPU use comparison')


''' ind cpu util plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 6]))), '--', label='CPU use peer2 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 10]))), '--', label='CPU use peer2 org 1')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 14]))), '--', label='CPU use peer1 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 18]))), '--', label='CPU use peer0 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 22]))), '--', label='CPU use peer0 org 1')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('CPU use in %')
ax2.set_ylabel('# of users')
ax1.set_title('CPU usage at data size 5')


''' avg mem util plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res2[1:61:, 3]))), '--', label='Avg. Mem. use for data size 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 3]))), '--', label='Avg. Mem. use for data size 5')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res8[1:61:, 3]))), '--', label='Avg. Mem. use for data size 8')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Mem. use in %')
ax2.set_ylabel('# of users')
ax1.set_title('Avg. Mem. use comparison')


''' ind mem util plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 7]))), '--', label='Mem. use peer2 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 11]))), '--', label='Mem. use peer2 org 1')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 15]))), '--', label='Mem. use peer1 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 19]))), '--', label='Mem. use peer0 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 23]))), '--', label='Mem. use peer0 org 1')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Mem. use in %')
ax2.set_ylabel('# of users')
ax1.set_title('Mem. usage at data size 5')


''' avg nw in plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res2[1:61:, 4]))), '--', label='Network input for data size 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 4]))), '--', label='Network input for data size 5')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res8[1:61:, 4]))), '--', label='Network input for data size 8')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Network input in Bytes')
ax2.set_ylabel('# of users')
ax1.set_title('Avg. network input comparison')


''' ind new in plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 8]))), '--', label='Network input peer2 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 12]))), '--', label='Network input peer2 org 1')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 16]))), '--', label='Network input peer1 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 20]))), '--', label='Network input peer0 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 24]))), '--', label='Network input peer0 org 1')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Network input in Bytes')
ax2.set_ylabel('# of users')
ax1.set_title('Network input at data size 5')


''' avg nw out plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res2[1:61:, 5]))), '--', label='Network output for data size 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 5]))), '--', label='Network output for data size 5')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res8[1:61:, 5]))), '--', label='Network output for data size 8')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Network output in Bytes')
ax2.set_ylabel('# of users')
ax1.set_title('Avg. network output comparison')


''' ind new out plot '''
fig, ax1 = plt.subplots(figsize=(15,10))
ax2 = ax1.twinx()
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 9]))), '--', label='Network output peer2 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 13]))), '--', label='Network output peer2 org 1')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 17]))), '--', label='Network output peer1 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 21]))), '--', label='Network output peer0 org 2')
ax1.plot(np.arange(0, 60), np.array(list(map(np.float, res5[1:61:, 25]))), '--', label='Network output peer0 org 1')
ax2.plot(np.arange(0, 60), np.array(list(map(np.float, metrics2[1::, 1]))), 'r-', label='# of users')
fig.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.25, -0.435, 0.5, 0.5))
ax1.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax2.set_xticklabels([0, 0, 100, 200, 300, 400, 500, 600])
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Network output in Bytes')
ax2.set_ylabel('# of users')
ax1.set_title('Network output at data size 5')
plt.show()


print("hi")
