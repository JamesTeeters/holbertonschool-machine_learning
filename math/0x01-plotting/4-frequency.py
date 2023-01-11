#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

bin_points = [40, 50, 60, 70, 80, 90, 100]
plt.hist(student_grades, bins=bin_points, edgecolor='black')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
plt.xlim(0, 100)
plt.xticks(range(0, 110, 10))
plt.ylim(0, 30)
plt.show()
