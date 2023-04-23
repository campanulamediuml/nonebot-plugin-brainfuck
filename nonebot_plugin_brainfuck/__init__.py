from nonebot import  on_startswith
from nonebot.adapters.onebot.v12 import GroupMessageEvent
from nonebot.plugin import PluginMetadata
from brainfuck_interpreter import call
from nonebot.matcher import Matcher

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_brainfuck",
    description="brainfuck解释器，brainfuck是一种仅含有八个字符的图灵完备语言",
    usage="在qq中进行交互对brainfuck代码进行解释",
    extra={},
)

command = on_startswith('nonebot_plugin_brainfuck:')

@command.handle
def brainfuck(event: GroupMessageEvent, matcher: Matcher):
    command = event.message.extract_plain_text().replace('nonebot_plugin_brainfuck:','')
    res:str = call(command)
    matcher.send(res,at_sender=True)

if __name__ == '__main__':
    r = call(
        '>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.')
    print(r)



