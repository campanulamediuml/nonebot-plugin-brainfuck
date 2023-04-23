import nonebot_plugin_brainfuck

def test_normal_input():
    r = nonebot_plugin_brainfuck.call(',>,+++++++++.<.:ab')
    print(r)

def test_normal_noinput():
    r = nonebot_plugin_brainfuck.call('>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.')
    # Hello, World!
    print(r)

def test_err_command():
    r = nonebot_plugin_brainfuck.call(',>,++++++++a+.<.:ab')
    # 打孔中包含错误指令
    print(r)

def test_err_inbox():
    r = nonebot_plugin_brainfuck.call(',>,+++++++++.<.:a')
    # 输入数据错误
    print(r)

if __name__ == '__main__':
    test_err_command()
    test_err_inbox()
    test_normal_noinput()