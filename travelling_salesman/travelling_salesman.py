



def distance(pt1, pt2):
    
  ## Squared distance function
    
  dist = (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2
  return dist

def score_solution(index):
    
  ## Calculate the distance of the current solution
    
  tot_dist = 0.
  for iii in range(len(index) - 1):
    id1 = index[iii]
    id2 = index[iii+1]
    tot_dist = tot_dist + distance(points[id1], points[id2])
  return tot_dist


def propose_new_state(curr_index):
    
  ## Propose a new state by switching two cities
    
  all_inds = [iii for iii in range(1, len(curr_index) - 1)]
  random.shuffle(all_inds)
  ind1 = all_inds[0]
  ind2 = all_inds[1]
  prop_index = copy.copy(curr_index)
  val1 = prop_index[ind1]
  val2 = prop_index[ind2]
  prop_index[ind1] = val2
  prop_index[ind2] = val1
  return prop_index

import copy
import random
import time

num_points_list = [10, 15, 20, 25]

for num_points in num_points_list:

  ## Initialize city positions
  points = [(random.random(),random.random()) for iii in range(num_points)]


  s_min = 1e10
  num_restarts = 10
  num_iters = 10000

  for ttt in range(num_restarts):
    city_list = [jjj for jjj in range(1,len(points))]
    random.shuffle(city_list)
    index = [0] + city_list + [0]
    first_index = copy.copy(index)
    curr_index = index
    
    ## Run MCMC scheme
    for jjj in range(num_iters):

      prop_index = propose_new_state(curr_index)

      s_curr = score_solution(curr_index)
      s_prop = score_solution(prop_index)
      u = random.random()
      if u < (s_curr - s_prop):
        curr_index = copy.copy(prop_index)
      else:
        pass
      
      if s_curr < s_min:
        s_min = s_curr
        best_index = copy.copy(curr_index)


  ## Run the plotting
  import matplotlib.pyplot as plt
  figure, ax = plt.subplots(1,2, figsize=(10,4))

  for x,y in points:
    ax[0].plot(x,y, 'ro')
    ax[1].plot(x,y, 'ro')

  for iii in range(len(index) - 1):
    id1 = best_index[iii]
    id2 = best_index[iii+1]
    ax[1].plot([points[id1][0], points[id2][0]], [points[id1][1], points[id2][1]], 'k')
    ax[1].set_title('(After MCMC) Travelled distance: {:.2f}'.format(score_solution(best_index)), fontsize=14)

  for iii in range(len(index) - 1):
    id1 = first_index[iii]
    id2 = first_index[iii+1]
    ax[0].plot([points[id1][0], points[id2][0]], [points[id1][1], points[id2][1]], 'k')
    ax[0].set_title('(Random) Travelled distance: {:.2f}'.format(score_solution(first_index)), fontsize=14)
  figure.suptitle('Num cities: {}'.format(num_points), fontsize=14, position = (0.5,1))

