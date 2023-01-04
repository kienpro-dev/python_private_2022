import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# x = np.array([1, 4, 3, 2])
# y = np.array([2, 0, 8, 7])
# plt.plot(x, y); # Lấy ví dụ điểm truyền vào sẽ được tô đậm

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.xlabel("Horizontal")
# plt.ylabel("Vertical")
# plt.title("X and Y")
# plt.plot(x, y)

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 4, 4, 1, 1])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("X and Y")
# plt.grid()
# plt.plot(x, y)

# plt.plot([1, 2], [3, 4], color="red")
x = np.linspace(0, 10, 1000)
plt.xlabel("X")
plt.ylabel("F(X)")
plt.title("Sin and Cos")
plt.plot(x, np.cos(x), label="cosx", color="blue");
plt.plot(x, np.sin(x), label="sinx", color="red");
plt.axis("Equal")
plt.legend()
plt.grid()
plt.show()