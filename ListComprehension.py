/*

Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, 

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 

*/

x,y,z,n = [input() for _ in range(4)]
print [[x,y,z] for x in range(x+1) for y in range(y+1) for z in range(z+1) if x+y+z!=n]
