import numpy as np

def calculate(ls:list):
  if len(ls) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    x = np.array(ls).reshape((3,3))
    mean_ = [x.mean(axis=0).tolist(),x.mean(axis=1).tolist(), x.mean().tolist()]
    var_ = [x.var(axis=0).tolist(),x.var(axis=1).tolist(), x.var().tolist()]
    std_ = [x.std(axis=0).tolist(),x.std(axis=1).tolist(), x.std().tolist()]
    max_ = [x.max(axis=0).tolist(),x.max(axis=1).tolist(), x.max().tolist()]
    min_ = [x.min(axis=0).tolist(),x.min(axis=1).tolist(), x.min().tolist()]
    sum_ = [x.sum(axis=0).tolist(),x.sum(axis=1).tolist(), x.sum().tolist()]
    calculations = {
    'mean': mean_,
    'variance': var_,
    'standard deviation': std_,
    'max': max_,
    'min': min_,
    'sum': sum_
    }

    return calculations
