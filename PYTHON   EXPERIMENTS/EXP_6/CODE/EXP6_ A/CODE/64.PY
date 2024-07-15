import matplotlib.pyplot as plt
import numpy as np

x = np.array(["CNND\n MS.SEEMA LADHE","AT\n MR.NILESH MAIL","MATHS\n MS.DAIMI MARIYA","COA \n MS.NEETA INGLE","OS\n MR.PRAVIN PATIL"])
y = np.array([75, 79,70,68,65])

plt.bar(x, y)
plt.bar(x, y, color = "#4CAF50",width = 0.3)
plt.ylabel("  AKASH  MARKS  SCORE")
plt.xlabel("\n SUBJECTS  TEACHER")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
