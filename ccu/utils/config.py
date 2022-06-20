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

from rich.console import Console

console = Console()


def parse_args():
    """
    Parsing arguments
    :return:
    """
    parser = argparse.ArgumentParser("PyTorch Image Captioning")
    parser.add_argument("--epochs", type=int, default=2000, help="number of epochs of training")
    parser.add_argument("--start_epoch", type=int, default=-1, help="epoch to start training from")
    parser.add_argument("--dataset", type=str, default="DIV2K", help="name of the dataset")
    parser.add_argument("--batch_size", type=int, default=1, help="size of the batches")
    parser.add_argument("--lr", type=float, default=0.0002, help="adam: learning rate")
    parser.add_argument("--num_worker", type=int, default=8,
                        help="number of cpu threads to use during batch generation")
    parser.add_argument("--img_height", type=int, default=256, help="size of image height")
    parser.add_argument("--img_width", type=int, default=256, help="size of image width")
    parser.add_argument("--channels", type=int, default=3, help="number of image channels")
    parser.add_argument("--checkpoint_interval", type=int, default=10, help="interval between saving model checkpoints")
    parser.add_argument("--save_dir", type=str, default='runs', help='Path for saving results')
    parser.add_argument("--cuda", action='store_false', help='Use cuda?')
    return check_args(parser.parse_args())


def check_args(args: argparse.Namespace) -> argparse.Namespace:
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
    args.cuda = True if args.cuda else False

    # 创建runs文件夹
    args.exp_dir = make_runs_dir(args, sub_dirs=['images', 'logs', 'checkpoints'])
    args.run_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
    console.print(args)
