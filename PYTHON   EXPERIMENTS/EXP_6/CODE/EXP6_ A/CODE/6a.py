import matplotlib.pyplot as ary
import numpy as a1

y=a1.array([75, 79,70,68,65])
mylabels = ["CNND\n MS.SEEMA LADHE","AT\n MR.NILESH MAIL","MATHS\n MS.DAIMI MARIYA","COA \n MS.NEETA INGLE","OS\n MR.PRAVIN PATIL"]
mycolors = [ "hotpink","r", "b", "#4CAF50","orange"]
myexplode = [0, 0.4, 0, 0,0]

ary.pie(y, labels = mylabels,autopct='%1.2f%%',colors = mycolors, explode = myexplode, shadow = True,startangle = -90)
ary.legend(title = "  % of AKASH YADAV \n   in TOTAL five subjects:")
#ary.pie(y, labels = mylabels,autopct='%1.2f%%')


ary.show()
