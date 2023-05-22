from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
import cv2
import numpy as np
# Invert the horse image
# image = invert(data.horse())
# print(image)

image=cv2.imread('I2.jpg')

# image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

height=image.shape[0]
width=image.shape[1]
Ratio=height/540


image=cv2.resize(image,(int(width/Ratio),int(height/Ratio)))
OgImage=cv2.resize(image,(int(width/Ratio),int(height/Ratio)))

# kernelSizes = [(3, 3), (9, 9), (15, 15)]

# image=cv2.blur(image, (100, 100))
# image=cv
OgImage=image
image=invert(image)

skeleton = skeletonize(image)

skeleton=np.array(skeleton)
skeleton=cv2.cvtColor(skeleton,cv2.COLOR_RGB2GRAY)


skeleton=invert(skeleton)
image=invert(image)
# fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(8, 4),
#                          sharex=True, sharey=True)

# ax = axes.ravel()


# ax[0].imshow(OgImage, cmap=plt.cm.gray)
# ax[0].axis('off')
# ax[0].set_title('original', fontsize=20)

# ax[1].imshow(skeleton, cmap=plt.cm.gray)
# ax[1].axis('off')
# ax[1].set_title('skeleton', fontsize=20)

# # ax[2].imshow(skeleton+OgImage, cmap=plt.cm.gray)
# # ax[2].axis('off')
# # ax[2].set_title('skeleton2', fontsize=20)

# fig.tight_layout()
# plt.show()
cv2.imwrite('op.jpg',image)
cv2.imwrite('op_skeleton.jpg',skeleton)