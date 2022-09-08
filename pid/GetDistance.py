import numpy as np
import math

def cal_distance(position, target, psi):
    """计算纵向距离和横向距离

    Args:
        position: 当前车辆位置
        target: 目标点
        psi: 偏航角

    Returns:
        d_r: 纵向距离
        d_t: 横向距离
    """
    target = np.array(target)
    e_r = np.array ([math.cos(psi),math.sin(psi)])
    d_r = np.dot((target - position), e_r.T)
    d_t = math.sqrt(np.linalg.norm(position - target)**2-d_r**2)

    
    return d_r, d_t