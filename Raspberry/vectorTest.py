import numpy

vector = numpy.array([[4],
                      [2],
                      [1],
                      [9]])
vc = numpy.shape(4, 2, 1, 9)
print(vector)
print(vc)
print(str(hex(11)))

matrix = numpy.array([[1, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0]])

print(matrix)

product = numpy.matmul(matrix, vector)

print(product)
