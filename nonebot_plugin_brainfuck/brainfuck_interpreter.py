# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
import struct
from typing import List, Dict, Optional

import error_info

MOVE_L = '<'
MOVE_R = '>'
V_ADD = '+'
V_SUB = '-'
STD_O = '.'
STD_I = ','
LOOP_I = '['
LOOP_O = ']'

LAN_DESC_I = 'BrainFuckINBOX'
LAN_DESC_O = 'BrainFuckOUTBOX'

TAPE_LENGTH = 65536
MOD_DATA = 0
byte_mode = 2 ** 8


class Interpreter(object):

    def __init__(self):
        self.memory:List[int] = [0] * TAPE_LENGTH
        self.tape_string:str = ''
        self.pointer:int = 0
        self.executor_pointer:int = 0
        self.debug:bool = False
        self.command_table:Dict[str] = self.init_table()
        self.frame = True
        self.outbox:str = ''
        self.inbox:str = ''

    def init_table(self):
        command_table = {
            MOVE_L: self.move_l,
            MOVE_R: self.move_r,
            V_ADD: self.v_add,
            V_SUB: self.v_sub,
            STD_O: self.std_o,
            STD_I: self.std_i,
            LOOP_I: self.jump_r,
            LOOP_O: self.jump_l,
        }
        return command_table

    def move_l(self):
        self.pointer = (self.pointer - 1) % TAPE_LENGTH
        self.executor_pointer += 1

    def move_r(self):
        self.pointer = (self.pointer + 1) % TAPE_LENGTH
        self.executor_pointer += 1

    def v_add(self):
        self.memory[self.pointer] = (self.memory[self.pointer] + 1) % byte_mode
        self.executor_pointer += 1

    def v_sub(self):
        self.memory[self.pointer] = (self.memory[self.pointer] - 1) % byte_mode
        self.executor_pointer += 1

    def std_i(self):
        '''
        挨个读取inbox内数据
        :return:
        '''
        # raw_input = input('%s > ' % LAN_DESC_I)
        # inbox = list(map(int, str(raw_input).strip()[0].encode()[0:]))[0]
        if len(self.inbox) == 0:
            return error_info.INBOX_ERR
        inbox = struct.unpack('b',self.inbox[0].encode())[0]
        self.inbox = self.inbox[1:]
        self.memory[self.pointer] = inbox % byte_mode
        self.executor_pointer += 1

    def std_o(self):
        # 挨个输出outbox内数据
        value: int = self.memory[self.pointer]
        if 0 <= value < 128:
            outbox = value.to_bytes(1, "little").decode()
        else:
            outbox = 'Not_ASCII'
        self.outbox += outbox
        self.executor_pointer += 1

    def jump_r(self):
        """
        跳转
        :return:
        """
        start_loop = 1
        cur_executor = self.executor_pointer
        if self.memory[self.pointer] != 0:
            self.executor_pointer += 1
            return
        while start_loop > 0:
            cur_executor += 1
            if self.tape_string[cur_executor] == LOOP_I:
                start_loop += 1
            if self.tape_string[cur_executor] == LOOP_O:
                start_loop -= 1
        self.executor_pointer = cur_executor
        self.executor_pointer += 1

    def jump_l(self):
        """
        跳转
        :return:
        """
        end_loop = 1
        cur_executor = self.executor_pointer
        if self.memory[self.pointer] == 0:
            self.executor_pointer += 1
            return
        while end_loop > 0:
            cur_executor -= 1
            if self.tape_string[cur_executor] == LOOP_O:
                end_loop += 1
            if self.tape_string[cur_executor] == LOOP_I:
                end_loop -= 1
        self.executor_pointer = cur_executor
        self.executor_pointer += 1

    def execute(self, tape:str) -> Optional[str]:
        tape = tape.split('//')[0].strip()
        tape = tape.replace(' ', '').replace('\n', '')
        for i in tape:
            if i not in self.command_table:
                return error_info.INVALID_COMMAND
        self.tape_string += tape
        while 1:
            if self.executor_pointer >= len(self.tape_string):
                return
            # print(self.executor_pointer,len(self.tape_string))
            command = self.tape_string[self.executor_pointer]
            func = self.command_table.get(command)
            if func is None:
                return error_info.INVALID_COMMAND
            r = func()
            if r is not None:
                return r

def call(command:str)->str:
    intp = Interpreter()
    tape = command.split(':')[0].strip()
    if len(command.split(':')) > 1:
        inbox = command.split(':')[1].strip()
        intp.inbox = inbox
    result = intp.execute(tape)
    if result is not None:
        return result
    return intp.outbox
