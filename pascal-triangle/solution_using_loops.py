import os
import sys

if(os.path.exists("input.txt")):
	sys.stdin = open("input.txt","r")
	sys.stdout = open("output.txt","w")

n_rows = int(input())

def generate_pascal_triangle(n_rows):
	triangle = []
	for i in range(n_rows):
		current_row = [] 
		for j in range(i+1):
			if j==0 or j == i:
				current_row.append(1)
			else:
				current_row.append(triangle[i-1][j-1] + triangle[i-1][j])
		triangle.append(current_row)
	return triangle

print(generate_pascal_triangle(n_rows))		

