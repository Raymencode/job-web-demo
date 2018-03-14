#!/usr/bin/env python
# -*- coding: utf-8 -*-

from job_spider.process import SpiderProcess, WriterProcess
from multiprocessing import Queue
import time


def main():
    queue = Queue()
    p1 = SpiderProcess(queue)
    p2 = WriterProcess(queue)
    p1.start()
    p2.start()
    while p2.is_alive():
        time.sleep(1)
    p1.terminate()


if __name__ == '__main__':
    main()
