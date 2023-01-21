import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

dpath = r'reading files and displaying data\data\lakemaywalk.csv'
mpath = r'reading files and displaying data\lakemap.png'
df = pd.read_csv(dpath)

class GPS(object):
    def __init__(self, dpath, mpath, points):
        self.dpath = dpath
        self.points = points
        self.mpath = mpath

        self.result_image = Image
        self.x_ticks = []
        self.y_ticks = []

    def plot_map(self, output='save', save_as = r'reading files and displaying data\NewMap.png'):
        # plots the map
        self.get_ticks()
        fig, axis1 = plt.subplots(figsize=(10, 10))
        axis1.imshow(self.result_image)
        axis1.set_xlabel('Longitude')
        axis1.set_ylabel('Latitude')
        axis1.set_xticklabels(self.x_ticks)
        axis1.set_yticklabels(self.y_ticks)
        axis1.grid()
        if output == 'save':
            plt.savefig(save_as)
        else:
            plt.show()

    def create_image(self, color, width=2):
        # saves NewMap with GPS data
        data = pd.read_csv(self.dpath, names=['LATITUDE', 'LONGITUDE'], sep=',')

        self.result_image = Image.open(self.mpath, 'r')
        img_points = []
        gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))
        for d in gps_data:
            x1, y1 = self.scale_to_img(d, (self.result_image.size[0], self.result_image.size[1]))
            img_points.append((x1, y1))
        draw = ImageDraw.Draw(self.result_image)
        draw.line(img_points, fill=color, width=width)

    def scale_to_img(self, lat_lon, h_w):
        # scales coordinates to image pixels
        old = (self.points[2], self.points[0])
        new = (0, h_w[1])
        y = ((lat_lon[0] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
        old = (self.points[1], self.points[3])
        new = (0, h_w[0])
        x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
        return int(x), h_w[1] - int(y)

    def get_ticks(self):
        # marks map with given coordinates
        self.x_ticks = map(lambda x: round(x, 4), np.linspace(self.points[1], self.points[3], num=10))
        y_ticks = map(lambda x: round(x, 4), np.linspace(self.points[2], self.points[0], num=10))
        self.y_ticks = sorted(y_ticks, reverse=True)


# points = (top, left, bottom, right)
vis = GPS(dpath, mpath, points = (28.8780, -81.6400, 28.8680, -81.6250))

vis.create_image(color=(255, 0, 0), width=5)

vis.plot_map(output='save')

print()