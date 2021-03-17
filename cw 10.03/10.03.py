from PIL import Image
import matplotlib.pyplot as plt

with Image.open("mem.jpg") as img:
  orig_width, orig_height = img.size
  width = 80
  scale = width / orig_width
  height = int(scale * orig_height)
  img.thumbnail((width, height))

  plt.imshow(img)
  plt.show()

a = [1,2,3,4,5,6,7,8,9,10,11,12]
def reshape(dellist, width, height):
    result_list = []

    for j in range(height):
        list_a = []
        result_list.append(list_a)
        for i in range(width*j, width * (j+1)):
            list_a.append(dellist[i])
    return result_list
print(reshape(a,4,3))
