def point_generator(n):
    points = []
    for i in range(n):
        x = float(input("Enter the x-value for a point: "))
        y = float(input("Enter the y-value for a point: "))
        points.append((x,y))
    return points

def lagrange_interpolation(points):
    coeff = []
    denominator = 1
    for i in range(len(points)):
        denominator = 1
        for j in range(len(points)):
            k = len(points) - j - 1
            if k != i:
                denominator *= (points[i][0] - points[k][0])
        coefficient = (points[i][1])/(denominator)
        coeff.append(coefficient)

    for i in range(len(coeff)):
        streng = ""
        for j in range(len(coeff)):
            k = len(points) - j - 1
            if k != i:
                streng += f'(x - {points[k][0]})'
        print(f'{coeff[i]}*{streng} + ')
    print("0")


point = point_generator(3)
lagrange_interpolation(point)
