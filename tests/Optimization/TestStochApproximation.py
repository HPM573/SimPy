import SimPy.Optimization as Opt
from tests.Optimization import ToyModels
import numpy as np

# create an object for the stochastic approximation method
mySimOpt = Opt.StochasticApproximation(
    sim_model=ToyModels.Xto2(err_sigma=10),
    derivative_step=1,
    step_size=Opt.StepSize(a=25))

# find the minimum
mySimOpt.minimize(max_itr=1000, x0=np.array([-50, 5]))

# plot x and objective function values
mySimOpt.plot_f_itr(f_star=0)
mySimOpt.plot_x_irs(x_star=[0, 0])

print(mySimOpt.itr_x)