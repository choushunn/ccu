# -*- coding: utf-8 -*-
"""
@Time       : 2022/06/17 11:28
@Author     : Spring
@FileName   : config.py
@Description: 
"""
import argparse
import datetime
import json
import os
import platform

import torch
from rich.console import Console

console = Console()


def parse_args():
    """
    Parsing arguments
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='GAN', choices=['GAN', 'WGAN'], help='model name')
    parser.add_argument('--datasets', type=str, default='datasets', help='data directory')
    parser.add_argument('--epochs', type=int, default=10, help='number of epochs')
    parser.add_argument('--batch_size', type=int, default=64, help='batch size')
    parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
    parser.add_argument('--optimizer', type=str, default='adam', help='optimizer')
    parser.add_argument('--loss', type=str, default='l1', choices=[], help='loss')
    parser.add_argument('--hyp', type=str, default='', help='yaml file')
    parser.add_argument('--resume', type=str, default='', help='resume from checkpoint')
    parser.add_argument('--weights', type=str, default='', help='weights')
    parser.add_argument('--pretrained', action='store_true', help='use pretrained model')
    parser.add_argument('--num_workers', type=int, default=int(os.cpu_count() * 3 / 4), help='number of workers')
    parser.add_argument('--save_dir', type=str, default='runs', help='save directory')
    parser.add_argument('--cuda', action='store_false', help='use cuda')
    parser.add_argument('--log_interval', type=int, default=10, help='log interval')
    parser.add_argument('--save_interval', type=int, default=10, help='save interval')
    parser.add_argument('--save_best', action='store_true', help='save best model')
    return check_args(parser.parse_args())


def check_args(args):
    """
    Checking arguments
    :param args:
    :return:
    """
    # --epoch
    assert args.epochs >= 1, console.print('Number of epochs must be larger than or equal to one',
                                           style='bold red')

    # --batch_size
    assert args.batch_size >= 1, console.print('Batch size must be larger than or equal to one',
                                               style='bold red')

    # --cuda
    args.cuda = args.cuda and torch.cuda.is_available()

    # 创建runs文件夹
    args.exp_dir = make_runs_dir(args, sub_dirs=['images', 'logs', 'checkpoints'])
    args.run_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    args.platform = platform.system()
    # save config
    json.dump(vars(args), open(os.path.join(args.exp_dir, 'args.json'), 'w'))
    return args


def make_runs_dir(args, sub_dirs: list = None):
    """
    Make runs directory
    :param sub_dirs:需要创建的子文件夹
    :param args:命令行参数
    :return:
    """
    if not args.save_dir:
        raise ValueError('Please provide a save directory using --save_dir')

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    exp_dirs_list = os.listdir(args.save_dir)

    if not exp_dirs_list:
        exp_id = 1
    else:
        exp_id = max([int(exp.split('_')[-1]) for exp in exp_dirs_list]) + 1

    exp_name = 'exp_' + str(exp_id)

    exp_dir = os.path.join(args.save_dir, exp_name)
    if not os.path.exists(exp_dir):
        os.makedirs(exp_dir)

    # create sub directory
    for sub_dir in sub_dirs:
        if not os.path.exists(os.path.join(exp_dir, sub_dir)):
            os.makedirs(os.path.join(exp_dir, sub_dir))
    console.print(f'The {exp_dir} directory is created successfully.', style='bold green')
    return exp_dir


if __name__ == '__main__':
    args = parse_args()
