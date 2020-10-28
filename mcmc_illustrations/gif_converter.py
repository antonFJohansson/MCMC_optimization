
## Convert images to gif
import imageio
import os

## Convert collection of images into a gif

filenames = []
for kkk in range(6000):
        filenames.append(str(kkk) + 'a' + '.png')
        filenames.append(str(kkk) + 'b' + '.png')


images = []
for filename in filenames:
    try:
        images.append(imageio.imread(os.path.join('full_illu_max',filename)))
    except:
        pass
imageio.mimsave('movie_b.gif', images)