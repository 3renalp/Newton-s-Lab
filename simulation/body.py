class body:

    def __init__(self,pos,velocity,rotation,rotation_velocity,mass,elasticity,isStatic,shape,isCircle=False,radius=0):
        self.pos=pos;
        self.velocity=velocity;
        self.rotation=rotation;
        self.rotation_velocity=rotation_velocity;
        self.mass=mass;
        self.elasticity=elasticity;
        self.isStatic=isStatic;
        self.shape=shape;
        self.loc=shape;
        self.isCircle=isCircle;
        self.radius=radius;
        self.update=False;

    def collusion(self,obj):
        if(self.isCircle and obj.isCircle):
            return self.collusionCC(obj);

    def collusionCC(self,obj):
        if(self.pos.distv(obj.pos)>(self.radius+obj.radius)):
            return False;
        return True;