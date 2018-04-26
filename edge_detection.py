from scipy import misc
import matplotlib.pyplot as plt

print ('test')

img = misc.face()
misc.imsave('.png,f')

plt.imshow(img)
plt.show 