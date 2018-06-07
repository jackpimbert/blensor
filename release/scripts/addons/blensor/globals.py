def getPixelPerMillimeter(width,height,sensor_size=32):
    long_edge = max(width,height)
    return long_edge/sensor_size


