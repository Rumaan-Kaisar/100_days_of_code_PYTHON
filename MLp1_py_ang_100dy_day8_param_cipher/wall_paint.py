import math

test_h = int(input("Height of wall: ")) 
test_w = int(input("Width of wall: ")) 
coverage = 5

def paint_calc(height, width, cover) : 
    caNumber = math.ceil((height*width)/cover)
    print(f"\n\t To paint your wall you need {caNumber} can paint")

paint_calc(height=test_h, width=test_w, cover=coverage)

# python wall_paint.py