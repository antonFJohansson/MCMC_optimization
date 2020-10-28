

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import os

## The distribution that we want to sample from
x = np.linspace(-5,7,1000)
y = 0.4*norm.pdf(x, -1, 0.5) + 0.6*norm.pdf(x, 3, 1)


def plot_one_iter(curr_x, new_x, store_x, first_iter, save_iter, save_folder = 'full_illu_max', max_pt = None):
  
    ## Function to plot one iteration of MCMC
    
  figure0, ax0 = plt.subplots(1,1, figsize=(10,5))
  figure1, ax1 = plt.subplots(1,1, figsize=(10,5))
  ax0.plot(x,y ,linewidth = 3)
  ax1.plot(x,y ,linewidth = 3)
  curr_y = 0.4*norm.pdf(curr_x, -1, 0.5) + 0.6*norm.pdf(curr_x, 3, 1)
  new_y = 0.4*norm.pdf(new_x, -1, 0.5) + 0.6*norm.pdf(new_x, 3, 1)

  bins_list = np.linspace(-4, 6.5, 40).tolist()
  if max_pt is None:
      ax0.plot([100],[100], 'ko', markersize = 10, label = "Current state")
      ax1.plot([100],[100], 'ko', markersize = 10, label = "Current state")
      ax0.plot([100],[100], 'ks', markersize = 10, label = "Proposed state")
      ax1.plot([100],[100], 'ks', markersize = 10, label = "Proposed state")
      ax0.plot(curr_x, curr_y, 'ko', markersize = 10)
      ax0.plot(new_x, new_y, 'ks', markersize = 10)
  else:
      ax0.plot([100],[100], 'ko', markersize = 10, alpha = 0.5, label = "Current state")
      ax1.plot([100],[100], 'ko', markersize = 10, alpha = 0.5, label = "Current state")
      ax0.plot([100],[100], 'ks', markersize = 10, alpha = 0.5, label = "Proposed state")
      ax1.plot([100],[100], 'ks', markersize = 10, alpha = 0.5, label = "Proposed state")
      ax0.plot([100],[100], 'rD', markersize = 10, label = "Max observed value")
      ax1.plot([100],[100], 'rD', markersize = 10, label = "Max observed value")
      ax0.plot(curr_x, curr_y, 'ko', markersize = 10, alpha = 0.5)
      ax0.plot(new_x, new_y, 'ks', markersize = 10, alpha = 0.5)
  if not first_iter and max_pt is None:
      ax0.hist(store_x[:-1], density = True, bins = bins_list, ec='black', alpha = 0.65)
  elif not max_pt is None:
      max_y = 0.4*norm.pdf(max_pt, -1, 0.5) + 0.6*norm.pdf(max_pt, 3, 1)
      ax0.plot(max_pt, max_y, 'rD', markersize = 10)
      ## Plot max point here

  if store_x[-1] == new_x:
    if max_pt is None:
        ax1.plot([new_x, new_x], [0, new_y], 'g--' ,linewidth = 3)
        ax1.plot(new_x, new_y, 'ko', markersize = 10)
        
    else:
        ax1.plot(new_x, new_y, 'ko', markersize = 10, alpha = 0.5)
  else:
    
    if max_pt is None:
        ax1.plot([curr_x, curr_x], [0, curr_y], 'g--',linewidth = 3)
        ax1.plot(curr_x, curr_y, 'ko', markersize = 10)
        
    else:
        ax1.plot(curr_x, curr_y, 'ko', markersize = 10, alpha = 0.5)
  if max_pt is None:
      ax1.hist(store_x, density = True, bins = bins_list, ec='black', alpha = 0.65)
  else:
      ## plot max point here
      max_y = 0.4*norm.pdf(max_pt, -1, 0.5) + 0.6*norm.pdf(max_pt, 3, 1)
      ax1.plot(max_pt, max_y, 'rD', markersize = 10)
      
  def get_vertical(x, init_height, height):
    return [x, x], [init_height - height, init_height + height]



 
  ax0.set_ylim(-0.02, 0.4)
  ax0.set_xlim(-4, 6.5)
  ax1.set_ylim(-0.02, 0.4)
  ax1.set_xlim(-4, 6.5)
  init_height = 0
  marker_height = 0.01
  for iii in range(len(bins_list) - 1):
    x1 = bins_list[iii]
    x2 = bins_list[iii + 1]
    ax0.plot([x1,x2], [init_height, init_height], 'k')
    ax1.plot([x1,x2], [init_height, init_height], 'k')
    x_v, y_v = get_vertical(x1, init_height, marker_height)
    ax0.plot(x_v, y_v, 'k')
    ax1.plot(x_v, y_v, 'k')
  ax0.legend(prop = {'size': 10}, loc = 'upper right')
  ax1.legend(prop = {'size': 10}, loc = 'upper right')
  ax0.text(-3.7, 0.35, "Iteration {}".format(save_iter), size = 15) ## Had 35 in size
  ax1.text(-3.7, 0.35, "Iteration {}".format(save_iter), size = 15)
  figure0.savefig(os.path.join(save_folder, str(save_iter) + 'a' + '.png'))
  figure1.savefig(os.path.join(save_folder, str(save_iter) + 'b' + '.png'))


## Plotting is controlled here
np.random.seed(1)
num_iters = 5050
curr_x = np.random.normal(0,1)
iters_to_plot1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
iters_to_plot2 = [iii for iii in range(20,500, 5)]
iters_to_plot3 = [iii for iii in range(550,5100, 50)]
iters_to_plot = iters_to_plot1 + iters_to_plot2 + iters_to_plot3

store_x = []

max_pt = curr_x
max_y_val = 0.4*norm.pdf(curr_x, -1, 0.5) + 0.6*norm.pdf(curr_x, 3, 1)
for iii in range(0,num_iters):

  new_x = np.random.normal(curr_x,1.5)
  store_new_x = new_x
  store_curr_x = curr_x

  curr_score = np.log(0.4*norm.pdf(curr_x, -1, 0.5) + 0.6*norm.pdf(curr_x, 3, 1))
  new_score = np.log(0.4*norm.pdf(new_x, -1, 0.5) + 0.6*norm.pdf(new_x, 3, 1))
  score = np.exp(new_score - curr_score)
  

  u = np.random.uniform()
  #print(score)
  if u < score:
    curr_x = new_x
  else:
    curr_x = curr_x
  store_x.append(curr_x)
  curr_y_val = 0.4*norm.pdf(curr_x, -1, 0.5) + 0.6*norm.pdf(curr_x, 3, 1)
  
  if curr_y_val > max_y_val:
      max_y_val = curr_y_val
      max_pt = curr_x
  
  if iii in iters_to_plot:
      if iii == 0:
          plot_one_iter(store_curr_x, store_new_x, store_x, True, iii, max_pt = max_pt)
      else:
          plot_one_iter(store_curr_x, store_new_x, store_x, False, iii, max_pt = max_pt)

