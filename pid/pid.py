# import matplotlib.pyplot as plt

class PID_posi():
    """位置式实现
    """
    def __init__(self, k, target, upper, lower):
        self.kp, self.ki, self.kd = k

        self.e = 0  # error
        self.pre_e = 0  # previous error
        self.sum_e = 0  # sum of error

        self.target = target  # target
        self.upper_bound = upper    # upper bound of output
        self.lower_bound = lower    # lower bound of output

    def set_target(self, target):
        self.target = target

    def set_k(self, k):
        self.kp, self.ki, self.kd = k

    def set_bound(self, upper, lower):
        self.upper_bound = upper
        self.lower_bound = lower

    def cal_output(self, obs):   # calculate output
        self.e = self.target - obs

        output = self.e * self.kp + self.sum_e * \
            self.ki + (self.e - self.pre_e) * self.kd
        if output < self.lower_bound:
            output = self.lower_bound
        elif output > self.upper_bound:
            output = self.upper_bound

        self.pre_e = self.e
        self.sum_e += self.e
        return output

    def reset(self):
        # self.kp = 0
        # self.ki = 0
        # self.kd = 0

        self.e = 0
        self.pre_e = 0
        self.sum_e = 0
        # self.target = 0

    def set_sum_e(self, sum_e):
        self.sum_e = sum_e
