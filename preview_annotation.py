# -*- coding: utf-8 -*-

#########################################################
#
# Alejandro German
# 
# https://github.com/seralexger/clothing-detection-ecommerce-dataset
#
#########################################################


from __future__ import print_function
import sys
import numpy as np
from PIL import Image
import json
import glob
import argparse
import random
import argparse
import matplotlib
import os
import shutil
matplotlib.use('TKAgg',warn=False, force=True)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset", help="Dataset folder")
ap.add_argument("-a","--annotation", help="Annotation folder")
ap.add_argument("-r","--remove_folder", help="Remove folder")
args = vars(ap.parse_args())


idx = 0
img_list = list(glob.glob(args['dataset']+'/*'))


def press(event):
	global idx, img_list, ax
	sys.stdout.flush()
	if event.key == 'q':
		exit(0)
	if event.key == 'r':
		if not args['remove_folder']:
			print('Please write in args -r and the remove_folder')
		else:
			if not os.path.exists(args['remove_folder']):
			    os.makedirs(args['remove_folder'])
			img_path = img_list[idx]
			shutil.move(img_path, args['remove_folder']+'/'+img_path.split('/')[-1])
			img_list = list(glob.glob(args['dataset']+'/*'))
			ax.clear()
			img_path = img_list[idx]
			img_data = json.loads(open(args['annotation']+'/dataset'+'_'+img_path.split('/')[-2]+'_'+img_path.split('/')[-1].split('.')[0]+'.json').read())
			normal_img = Image.open(img_path)

			color_dic = {}
			for index,item in enumerate(img_data['arr_boxes']):
				if item['class'] not in color_dic:
					color_dic[item['class']] = (random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0))
				box = patches.Rectangle((item['x'], item['y']),  item['width'],  item['height'],linewidth=2,edgecolor=color_dic[item['class']] ,facecolor='none', label = item['class'])
				ax = fig.add_subplot(111)
				ax.add_patch(box)
				ax.legend()
				ax.imshow(normal_img)
				ax.axis('off')
			fig.canvas.draw()
	if event.key == 'n':
		if idx != len(img_list):
			idx+=1
		ax.clear()
		img_path = img_list[idx]
		img_data = json.loads(open(args['annotation']+'/dataset'+'_'+img_path.split('/')[-2]+'_'+img_path.split('/')[-1].split('.')[0]+'.json').read())
		normal_img = Image.open(img_path)

		color_dic = {}
		for index,item in enumerate(img_data['arr_boxes']):
			if item['class'] not in color_dic:
				color_dic[item['class']] = (random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0))
			box = patches.Rectangle((item['x'], item['y']),  item['width'],  item['height'],linewidth=2,edgecolor=color_dic[item['class']] ,facecolor='none', label = item['class'])
			ax = fig.add_subplot(111)
			ax.add_patch(box)
			ax.legend()
			ax.imshow(normal_img)
			ax.axis('off')
		fig.canvas.draw()
	if event.key == 'b':
		if idx != 0:
			idx-=1
		ax.clear()
		img_path = img_list[idx]
		img_data = json.loads(open(args['annotation']+'/dataset'+'_'+img_path.split('/')[-2]+'_'+img_path.split('/')[-1].split('.')[0]+'.json').read())
		normal_img = Image.open(img_path)

		color_dic = {}
		for index,item in enumerate(img_data['arr_boxes']):
			if item['class'] not in color_dic:
				color_dic[item['class']] = (random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0))
			box = patches.Rectangle((item['x'], item['y']),  item['width'],  item['height'],linewidth=2,edgecolor=color_dic[item['class']] ,facecolor='none', label = item['class'])
			ax = fig.add_subplot(111)
			ax.add_patch(box)
			ax.legend()
			ax.imshow(normal_img)
			ax.axis('off')
		fig.canvas.draw()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', press)

img_path = img_list[idx]
img_data = json.loads(open(args['annotation']+'/dataset'+'_'+img_path.split('/')[-2]+'_'+img_path.split('/')[-1].split('.')[0]+'.json').read())
normal_img = Image.open(img_path)


color_dic = {}
for index,item in enumerate(img_data['arr_boxes']):
	if item['class'] not in color_dic:
		color_dic[item['class']] = (random.uniform(0.0,1.0), random.uniform(0.0,1.0),random.uniform(0.0,1.0))
	box = patches.Rectangle((item['x'], item['y']),  item['width'],  item['height'],linewidth=2,edgecolor=color_dic[item['class']] ,facecolor='none', label = item['class'])
	ax.add_patch(box)
	ax.legend()
	ax.imshow(normal_img)
	ax.axis('off')


plt.show()