# Display trigonometric table of sin, cos and tan
import math
print(f"{'angle':>6} | {'sin':>6} | {'cos':>6}| {'tan':>6}")
for angle in range(0,361,30):
    rad=math.radians(angle)
    sin_val=math.sin(rad)
    cos_val=math.cos(rad)
    if math.isclose(cos_val,0.0,abs_tol=1e-9):
        tan_val="undefined"
    else:
        tan_val=f"{(math.tan(rad)):.2f}"
    print(f"{angle:>6} | {sin_val:>6.2f} | {cos_val:>6.2f} | {tan_val:>6}")