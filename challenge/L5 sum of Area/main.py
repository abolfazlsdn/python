def area_sum(rectangles):
    sumOfArea = 0
    for rectangle in rectangles:
        height = rectangle['height']
        width = rectangle['width']
        area = height* width
        sumOfArea += area
    return sumOfArea        