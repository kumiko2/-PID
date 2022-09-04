import numpy as np

def cal_target_index(car_posi, refer_path):
    """得到临近的路点

    Args:
        car_posi (_type_): 当前车辆位置
        refer_path (_type_): 参考轨迹（数组）

    Returns:
        _type_: 最近的路点的索引
    """
    dists = []
    for xy in refer_path:
        dis = np.linalg.norm(car_posi-xy)
        dists.append(dis)

    min_index = np.argmin(dists)
    return min_index
