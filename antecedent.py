from box import box

class antecedent():

    def __init__(self) -> None:
        self.key = []
        self.points = []
    
    def add(self,point, ant):
        self.seek_and_remove(point)
        self.key.append(ant)
        self.points.append(point)
    
    def seek_and_remove(self,point):
        for i in range(len(self.key)):
            if self.points[i]==point:
                del self.points[i]
                del self.key[i]
    
    def unstack(self):
        n = len(self.key)
        del self.key[n-1]
        del self.points[n-1]
    
    def get_key(self,point):
        for i in range(len(self.key)):
            if self.points[i]==point:
                return self.key[i]
    
