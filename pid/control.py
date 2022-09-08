import numpy as np
import matplotlib.pyplot as plt  
import matplotlib.pyplot as plt
from scipy.io import loadmat

from celluloid import Camera

from pid import PID_posi 
from CarModel import KinematicModel
from GetTarget import cal_target_index
from GetDistance import cal_distance

pid_delta = PID_posi([0,0,0], 8, 100, -100) 
pid_v = PID_posi([0,0,0], 8, 100, -100) 
car = KinematicModel(-354.74, -121.35, 0, 0, 10, 15) 

# 创建参考路径
refer_path = []
x1 = loadmat('global_path_x.mat')
y1 = loadmat('global_path_y.mat')
for i in range(len(y1['global_path_y'])):
    refer_path.append([x1['global_path_x'][i],y1['global_path_y'][i]])

fig = plt.figure(1)
# 保存动图用
camera = Camera(fig)

dt=0.1 # 每隔dt更新一次小车状态

x_ = []
y_ = [] # 记录小车轨迹

for i in range(550):
    # delay(dt)  延迟dt秒
    car_posi = np.zeros(2)
    car_posi[0] = car.x
    car_posi[1] = car.y
    target_index = cal_target_index(car_posi, refer_path)  # 查询离car_posi最近的点
    d_r, d_t = cal_distance(car_posi, refer_path[target_index], car.psi) # 计算纵向横向距离

    output_v = pid_v.cal_output(d_t) #后轮速度
    delta = pid_delta.cal_output(d_t) #前轮转角

    car.update_state(output_v, delta, dt)
    # 显示动图
    plt.cla()
    plt.plot(x1['global_path_x'], y1['global_path_y'], '-.b', linewidth=1.0)
    plt.plot(x_, y_, "-r", label="trajectory")
    plt.plot(car.x, car.y, "go", label="target")
    plt.grid(True)
    plt.pause(0.001)

plt.figure(2)
plt.plot(x1['global_path_x'], y1['global_path_y'], '-.b', linewidth=1.0)
plt.plot(x_,y_,'r')
plt.show()