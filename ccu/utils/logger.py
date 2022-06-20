import numpy as np
from matplotlib import pyplot as plt
from tensorboardX import SummaryWriter


class Logger(SummaryWriter):
    def __init__(self, log_dir):
        super(Logger, self).__init__(log_dir)
        self.writer = SummaryWriter(log_dir=log_dir)

    def close(self):
        self.writer.close()

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


def test():
    logger = Logger('./logs')
    fig, ax = plt.subplots()
    ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
    ax.set_title('Simple Scatter')
    # plt.show()
    logger.add_figure('test', fig)
    logger.add_text('test', 'test')
    logger.close()


if __name__ == '__main__':
    test()
