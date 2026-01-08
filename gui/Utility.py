def interpolate(p1, p2, t):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 * (1 - t) + x2 * t, y1 * (1 - t) + y2 * t)
