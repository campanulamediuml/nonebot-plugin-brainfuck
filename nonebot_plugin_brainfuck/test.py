# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
from brainfuck_bot.brainfuck_bot.plugins.nonebot_plugin_brainfuck.brainfuck_interpreter import call

if __name__ == '__main__':
    r = call('>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.')
    print(r)
