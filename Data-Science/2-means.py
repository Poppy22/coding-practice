class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []
    
    def update(self):
        sum_y = sum([point.y for point in self.points])
        sum_x = sum([point.x for point in self.points])
        mean_y = sum_y / len(self.points)
        mean_x = sum_x / len(self.points)
        self.center = Point(mean_x, mean_y)
        self.points = [] #remove previous points
        
    def add_point(self, point):
        if point not in self.points:
            self.points.append(point)

def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                # add the right point
                a.add_point(point)
            else:
                # add the right point
                b.add_point(point)
        if a_old == a.points:
            break
        a_old = a.points
        a.update()
        b.update()
        
    if a.center.x >= b.center.x:
        result = [(a.center.x, a.center.y), (b.center.x, b.center.y)]
    else:
        result = [(b.center.x, b.center.y), (a.center.x, a.center.y)]
    return result

