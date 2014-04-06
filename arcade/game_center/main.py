from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals


import time
import traceback
import threading
from collections import deque
from game_center.Application import Application


class MainQueueItem(object):
    done = False
    exception = None
    result = None


_main_thread = threading.currentThread()


class Main(object):

    queue = deque()
    lock = threading.Lock()

    @classmethod
    def process(cls):
        with cls.lock:
            for i in range(len(cls.queue)):
                item = cls.queue.popleft()
                try:
                    item.result = item.func(*item.args, **item.kwargs)
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    item.exception = e
                item.done = True

    @classmethod
    def call(cls, func, *args, **kwargs):
        if threading.currentThread() == _main_thread:
            return func(*args, **kwargs)
        item = MainQueueItem()
        item.func = func
        item.args = args
        item.kwargs = kwargs
        with cls.lock:
            cls.queue.append(item)
        while not item.done:
            time.sleep(0.01)
        if item.exception:
            raise item.exception
        return item.result


def main():
    #import logging; logging.shutdown(); import sys; sys.exit()
    print("Fengestad Game System...")
    Application()

    from game_center.gamecenter import GameCenter
    GameCenter.init()

    import game_center.glui
    game_center.glui.main()
    print(" --- game_center.glui.main is done ---")
    return
