import math

x1, y1, r1 = map(float, input("Enter the coordinates of the center (x1, y1) and radius (r1) of the first circle: ").split())
x2, y2, r2 = map(float, input("Enter the coordinates of the center (x2, y2) and radius (r2) of the second circle: ").split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distance > r1 + r2:
    result = "No intersection points (the circles are separate)."
elif distance < abs(r1 - r2):
    result = "No intersection points (one circle is inside the other)."
elif distance == 0 and r1 == r2:
    result = "Infinite points of intersection (the circles coincide)."
elif distance == r1 + r2 or distance == abs(r1 - r2):
    result = "One intersection point (the circles are tangent)."
else:
    result = "Two intersection points (the circles intersect)."

print(result)
