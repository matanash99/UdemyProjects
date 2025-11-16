import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Setup figure and axis
fig, ax = plt.subplots(figsize=(12, 4))
ax.set_xlim(0, 12)
ax.set_ylim(0, 2)
ax.axis('off')

# Computer A and B
ax.text(0, 1.5, "Computer A", fontsize=12, ha='center')
ax.text(11.5, 1.5, "Computer B", fontsize=12, ha='center')

# Draw computers
ax.add_patch(patches.Rectangle((0.3, 1.3), 1.4, 0.7, fill=True, color='lightblue'))
ax.add_patch(patches.Rectangle((10.3, 1.3), 1.4, 0.7, fill=True, color='lightgreen'))

# Draw line (the link)
ax.plot([1.7, 10.3], [1.65, 1.65], color='black', linewidth=2)
ax.text(6, 1.8, "2 Gbps link, RTT = 0.08 sec", ha='center', fontsize=10)

# Draw packets in transit
for i in range(15):
    x = 1.9 + i * 0.5
    ax.add_patch(patches.Rectangle((x, 1.45), 0.4, 0.3, fill=True, color='orange'))
    if i == 7:
        ax.text(x + 0.2, 1.3, "Packet (1200 bytes)", ha='center', fontsize=8)

# BDP label
ax.text(6, 1.0, "BDP = 160,000,000 bits", ha='center', fontsize=11, color='blue')
ax.text(6, 0.75, "Minimum window = 15,000 packets (for 90% utilization)", ha='center', fontsize=10, color='purple')

plt.title("TCP Window Size Visualization Based on BDP", fontsize=14)
plt.tight_layout()
plt.show()
