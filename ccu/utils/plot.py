# -*- coding: utf-8 -*-
"""
@Time       : 2022/06/05 21:33
@Author     : Spring
@FileName   : plot.py
@Description: 
"""
import cv2
import numpy as np
import torch
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


def plot3sub_images(images: list, sub_titles: list = None, title: str = None, is_show=False):
    """
    绘制对比图
    :param is_show:
    :param images:图像列表
    :param sub_titles:子图标题列表
    :param title:图标题
    :return:None
    """
    plt.figure(figsize=(16, 9), dpi=72)
    grid = plt.GridSpec(2, 2, wspace=0.4, hspace=0.3)
    for i in range(len(images)):
        if i == 0:
            plt.subplot(grid[:, 0])
        else:
            plt.subplot(grid[i - 1, 1])
        plt.imshow(images[i], cmap='gray')
        plt.title(sub_titles[i], fontsize=22)
        plt.axis("off")
        plt.xticks([])
        plt.yticks([])
    plt.suptitle(title, fontsize=22)
    if is_show:
        plt.show()
    else:
        plt.savefig(f"images/{title}.png")


def plot2sub_images(images: list, sub_titles: list, title: str = None):
    """
    绘制2对比图
    :param images:图像列表
    :param sub_titles:子图标题列表
    :param title:图标题
    :return:None
    """
    plt.figure(figsize=(16, 9), dpi=72)
    grid = plt.GridSpec(1, 2, wspace=0.4, hspace=0.3)
    for i in range(len(images)):
        plt.subplot(1, 2, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(sub_titles[i], fontsize=22)
        plt.axis("off")
        plt.xticks([])
        plt.yticks([])
    plt.suptitle(title, fontsize=22)
    plt.show()


def plot_image(image: np.ndarray, title: str = None, gray=False):
    """
    绘制图像
    :param gray:
    :param image:图像
    :param title:图标题
    :return:None
    """
    plt.imshow(image, cmap='gray' if gray else None)
    plt.title(title, fontsize=22)
    plt.axis("off")
    plt.xticks([])
    plt.yticks([])
    plt.show()


def save_gan_image(imgs, batches_done, path):
    """
    保存生成图像
    """
    real_A, fake_B, real_B = imgs
    for img in range(real_A.shape[0]):
        real_A_img = real_A[img].mul(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).to("cpu", torch.uint8).numpy()
        real_B_img = real_B[img].mul(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).to("cpu", torch.uint8).numpy()
        fake = fake_B[img].mul(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).to("cpu", torch.uint8).numpy()
        cv2.imwrite(f"{path}/{batches_done}_fake_{img}.png", fake)
        cv2.imwrite(f"{path}/{batches_done}_real_A_{img}.png", real_A_img)
        cv2.imwrite(f"{path}/{batches_done}_real_B_{img}.png", real_B_img)
        # plot3sub_images([real_A_img, real_B_img, fake], ["真实图像", "输入图像", "生成图像"],
        #                 f"{str(batches_done).zfill(5)}_" + "第" + str(img) + "张图像")
