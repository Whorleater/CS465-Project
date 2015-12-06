# generates random grades 
import numpy as np

youPerAssignment = np.random.randint(60, 100, size=7)
averagePerAssignment = np.random.randint(40, 90, size=7)

youAverage = []
classAverage = []

youAverage.append(youPerAssignment[0])
classAverage.append(averagePerAssignment[0])
for i in range(1, 7):
    youAverage.append((youPerAssignment[i] + sum(youAverage))/(len(youAverage)+1))
    classAverage.append((averagePerAssignment[i]+sum(classAverage))/(len(classAverage)+1))

print(youPerAssignment)
print(averagePerAssignment)

print("\n")
print(youAverage)
print(classAverage)