import math

class KinematicModel(object):
    """  自行车运动学模型

    Args:
        psi: 偏航角
        f_len: 前轮到车质心的距离
        r_len: 后轮到车质心的距离
        beta: 车质心速度与车身的夹角
        delta: 方向盘朝向与车身夹角
     """

    def __init__(self, x, y, psi, v, f_len, r_len):
        self.x = x
        self.y = y
        self.psi = psi
        self.v = v

        self.f_len = f_len
        self.r_len = r_len

    def get_state(self):
        return self.x, self.y, self.psi, self.v

    def update_state(self, v, delta, dt):
        beta = math.atan((self.r_len / (self.r_len + self.f_len)) * math.tan(delta))
        # sensor_v=[]
        # sensor_psi=[]
        # self.psi = sensor_psi
        # self.v = sensor_v
        self.v = v
        self.x = self.x + self.v * math.cos(self.psi * beta) * dt
        self.y = self.y + self.v * math.sin(self.psi * beta) * dt
        self.psi = self.psi + (self.v / self.f_len) * math.sin(beta) * dt
        return self.x, self.y, self.psi, self.v