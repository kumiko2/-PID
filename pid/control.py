import numpy as np

from pid import PID_posi 
from CarModel import KinematicModel
from GetTarget import cal_target_index
from GetDistance import cal_distance

pid_delta = PID_posi([0,0,0], 8, 100, -100) 
pid_v = PID_posi([0,0,0], 8, 100, -100) 
car = KinematicModel(0, 0, 0, 0, 10, 15) 
refer_path=[]
dt=0.1 # 每隔dt更新一次小车状态

# x_ = []
# y_ = [] 记录小车轨迹

while True:
    # delay(dt)  延迟dt秒
    car_posi = np.zeros(2)
    car_posi[0] = car.x
    car_posi[1] = car.y
    target_index = cal_target_index(car_posi, refer_path)  # 查询离car_posi最近的点
    d_r, d_t = cal_distance(car_posi, refer_path[target_index], car.psi) # 计算纵向横向距离

    output_v = pid_v.cal_output(d_t) #后轮速度
    delta = pid_delta.cal_output(d_t) #前轮转角

    car.update_state(delta, dt) 



