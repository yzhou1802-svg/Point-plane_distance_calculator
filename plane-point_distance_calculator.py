import math

def get_point(point_name):
    """获取一个三维点的坐标"""
    print(f"please enter the coordinates of{point_name}:")
    x = float(input('first number: '))
    y = float(input('second number: '))
    z = float(input('third number: '))
    point = [x, y, z]
    print(f'{point_name} is= ({x}, {y}, {z})')
    return point
#11行的代码用def保存计算函数的方法
def calculate_vector(p1, p2):
    """计算两点之间的向量"""
    return [p2[i] - p1[i] for i in range(3)]

# 主程序
ebenepunkt1 = get_point('P1')
ebenepunkt2 = get_point('P2')
ebenepunkt3 = get_point('P3')

e_vektor1 = calculate_vector(ebenepunkt1, ebenepunkt2)
e_vektor2 = calculate_vector(ebenepunkt1, ebenepunkt3)

print('The plane function is=', ebenepunkt1, '+ s*', e_vektor1, '+ t*', e_vektor2)
#normale 的坐标
cross_product=[
    e_vektor1[1]*e_vektor2[2]-e_vektor1[2]*e_vektor2[1],
    e_vektor1[2]*e_vektor2[0]-e_vektor1[0]*e_vektor2[2],
    e_vektor1[0]*e_vektor2[1]-e_vektor1[1]*e_vektor2[0],

]
print('cross_product is=', cross_product)


#要求的点的坐标
geb_punkt1=get_point(point_name='P4')


#Ebene的Koordinatenform
a,b,c=cross_product
x0,y0,z0=ebenepunkt1
d=a*x0+b*y0+c*z0
print('Coordinate form of the plane:')
print(f"{a}*x+{b}*y+{c}*z={d}")
#Gradegleichung以及在Parameterform中每个点的表达形式
p=ebenepunkt1
n=cross_product
print('line equation(vector form):')
print(f'x(k)=({p[0]}, {p[1]}, {p[2]}) + k*({n[0]}, {n[1]}, {n[2]})')

print("\nParameter form of the plane for x,y and z:")
print(f"x(k) = {p[0]} + k*{n[0]}")
print(f"y(k) = {p[1]} + k*{n[1]}")
print(f"z(k) = {p[2]} + k*{n[2]}")
#把每一个表达式再带回到Coordinate form里求变量k
n=cross_product
p=ebenepunkt1
num = d - (a * p[0] + b * p[1] + c * p[2])
den = a * n[0] + b * n[1] + c * n[2]

if den == 0:
    # 特殊情况，当分母为0的时候
    if num == 0:
        print("\nThe straight line is on the plane（with infinitely many points of intersection）.")
        intersection = None
        vector_geb_to_intersection = None
    else:
        print("\n The straight line does not intersect the plane (there are no points of intersection).")
        intersection = None
        vector_geb_to_intersection = None

else:
    k = num / den
    intersection = [p[i] + k * n[i] for i in range(3)]
    vector_geb_to_intersection = [intersection[i] - geb_punkt1[i] for i in range(3)]
    f_vector_geb_to_intersection = list(map(float, vector_geb_to_intersection))
print("The Vector from P4 to the intersection =", tuple(vector_geb_to_intersection))

x1, y1, z1 = f_vector_geb_to_intersection
distance_intersection_to_gebpunkt1=math.exp(0.5* math.log(x1**2.0+y1**2.0+z1**2.0))
print(f'The distance between intersection and the plane:',round(distance_intersection_to_gebpunkt1))


