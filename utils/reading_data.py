import os
import pickle

# dir = "disparity"
dir_training = '/home/kike/Documents/Dataset/ICCV_dataset/MP3D/train'
dir_image_up = dir_training + '/image_up'
dir_image_down = dir_training + '/image_down'
dir_disp = dir_training + '/disp_up'

dir_training = '/home/kike/Documents/Dataset/ICCV_dataset/MP3D/testing'

if not os.path.exists('./data'):
    os.makedirs("./data")

paths_image_up = []
paths_image_down = []
paths_disparity = []
for root, dirs, files in os.walk(dir_image_up):
    for file in files:
        paths_image_up.append(os.path.join(root, file))
for root, dirs, files in os.walk(dir_image_down):
    for file in files:
        paths_image_down.append(os.path.join(root, file))
for root, dirs, files in os.walk(dir_disp):
    for file in files:
        paths_disparity.append(os.path.join(root, file))

fout_up = open('./data/paths_up_train.pkl', 'wb')
fout_down = open('./data/paths_down_train.pkl', 'wb')
fout_disp = open('./data/paths_disp_train.pkl', 'wb')

pickle.dump(paths_image_up, fout_up)
pickle.dump(paths_image_down, fout_down)
pickle.dump(paths_disparity, fout_disp)

fout_up.close()
fout_down.close()
fout_disp.close()

