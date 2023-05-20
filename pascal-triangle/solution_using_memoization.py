import os
import sys

if (os.path.exists("input.txt")):
	sys.stdin = open("input.txt","r")
	sys.stdout = open("output.txt","w")

n_rows = int(input())

def generate_pascal_triangle(n_rows,memo):
	if n_rows in memo:
		return memo[n_rows]
	else:
		triangle = generate_pascal_triangle(n_rows-1,memo)
		prev_row = triangle[-1]
		current_row = []
		for i in range(len(prev_row)+1):
			if i == 0 or i == len(prev_row):
				current_row.append(1)
			else:
				current_row.append(prev_row[i-1]+prev_row[i])
	triangle.append(current_row)
	memo[n_rows] = triangle
	return triangle

print(generate_pascal_triangle(n_rows,memo={1:[[1]]}))