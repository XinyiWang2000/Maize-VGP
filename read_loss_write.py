import os
import matplotlib.pyplot as plt
import numpy as np

src_path = '/public/WangXinyi/Pix2PixHD/checkpoints'
# for dir_name in os.listdir(src_path):
for dir_name in ['20240122.2WXY']:
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    model_name = dir_name[4:-3]
    print(os.path.join(src_path, dir_name, 'loss_log.txt'))
    if os.path.exists(os.path.join(src_path, dir_name, 'loss_log.txt')):
        f = open(os.path.join(src_path, dir_name, 'loss_log.txt'), 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line[:6] != '(epoch':
                continue
            if len(x) == 200:
                break
            list = line.split(' ')
            lat_list = lines[i+1].split(' ')
            if float(list[1].replace(',', '')) == float(lat_list[1].replace(',', '')):
                continue
            x.append(float(list[1].replace(',', '')))
            y1.append(float(list[7]))
            y2.append(float(list[9]))
            y3.append(float(list[11]))
            y4.append(float(list[13]))
            y5.append(float(list[15]))
            if len(list) > 17:
                y6.append(float(list[17]))
            if len(list) > 18:
                y7.append(float(list[19]))
        plt.plot(x, np.array(y1), linestyle=':', color='k')
        plt.plot(x, np.array(y2), linestyle='-', color='k')
        plt.savefig(os.path.join('checkpoints/loss_imgs_0324', model_name + '_loss1.png'))
        plt.close()
        plt.plot(x, np.array(y4), linestyle='-', color='k')
        plt.plot(x, np.array(y5), linestyle=':', color='k')
        plt.savefig(os.path.join('checkpoints/loss_imgs_0324', model_name + '_loss2.png'))
        plt.close()
        plt.plot(x, np.array(y3), linestyle='-', color='k')
        if len(y6) != 0:
            plt.plot(x, np.array(y6), linestyle='-.', color='k')
        if len(y7) != 0:
            plt.plot(x, np.array(y7), linestyle=':', color='k')
        plt.savefig(os.path.join('checkpoints/loss_imgs_0324', model_name + '_loss3.png'))
        # plt.figure()
        f.close()