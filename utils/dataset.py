import pickle
import cv2
import numpy as np


class Dataset():

    def __init__(self, root_dir, settype):
        """
        :param root_dir: root of pkl files
        :param settype: train or testing
        """
        self.root_dir = root_dir
        self.settype = settype
        fin_up = open(self.root_dir + '/paths_up_' + settype + '.pkl', 'rb')
        fin_down = open(self.root_dir + '/paths_down_' + settype + '.pkl', 'rb')
        fin_disp = open(self.root_dir + '/paths_disp_' + settype + '.pkl', 'rb')

        self.paths_up = pickle.load(fin_up)
        self.paths_down = pickle.load(fin_down)
        self.paths_disp = pickle.load(fin_disp)

        self.paths_up.sort()
        self.paths_down.sort()
        self.paths_disp.sort()

        fin_up.close()
        fin_down.close()
        fin_disp.close()
        self.len = len(self.paths_up)

    def __len__(self):
        return self.len

    def get_data(self, idx):

        image_up = cv2.imread(self.paths_up[idx])#.reshape(540, 960, 3)  # .transpose((2, 0, 1))
        image_up = cv2.resize(image_up, (960, 540))
        image_down = cv2.imread(self.paths_down[idx])#.reshape(540, 960, 3)  # .transpose((2, 0, 1))
        image_down = cv2.resize(image_down, (960, 540))
        disp = np.load(self.paths_disp[idx])# .astype(np.uint8).reshape(540, 960, 1).transpose((2, 0, 1))
        disp = cv2.resize(disp, (960, 540))
        sample = {'up': image_up, 'down': image_down, 'disp': disp}
        return sample
