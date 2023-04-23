<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-brainfuck

_✨ brainfuck解释器，让你甚至可以在QQ上写图灵完备的代码 ✨_

### 使用方法

群聊中使用  brainfuck:{语句}:输入

如 brainfuck:,>,++.<.:ab

可以得到输出 da


### 关于brainfuck

这是一句helloworld
```brainfuck
++++++++[>++++[>++>+++>+++>+>+<<<<<-]>+>+>->+[<]<-]>>.>---.+++++++..+++.>>++++.>.<<-.<.+++.------.--------.>>>+.

```

你别笑！这可是图灵完备的语言！如果你愿意，甚至可以等价翻译成简单的汇编

### 简单的brainfuck语法

brainfuck可以理解为是对图灵机的完全模拟

计算机对指令纸带上逐个符号进行执行，同时计算机内拥有一条有限或无限长度的内存，每一个位置的数据都为0，指针初始位置指向地址为0的内存块

```
> 内存指针右移一个地址

< 内存指针左移一个地址

+ 当前指针指向的内存块内的数据+1

- 当前指针指向的内存块内的数据-1

. 把当前内存块内的数据输出到控制台

, 从控制台读取一个小于2^8的数字，写入控制台(本解释器中输入一个大于255的数字会被自动取256模)

[ 如果当前指针指向的内存块数据为0，则跳转到对应的]后执行

] 如果当前指针指向的内存块数据不为0，则跳转到对应的[后执行
```

看，语法很简单吧，现在，我们可以尝试着用brainfuck写一个简单的减法器了

```
,>++++++[<-------->-]<.
```

首先读取控制台中的一个数储存在地址0内，左移一格内存，在地址1的内存中写入6作为计数器，之后回到储存数字的内存地址，进行8次-1，然后令计数器-1，直到计数器归零后输出地址0的数字
等于对地址0进行了6次批量-1的计算，每次计算为8次-1，总计6*8 = 48次减一

同理

```
,>++++++++[<------>-]<.
```

也能输出完全相同的结果

现在你对brainfuck或者打孔编程有一点简单的概念了吧？好了，我们开始尝试着用它来写一个网络app，或者做个3A游戏吧！


