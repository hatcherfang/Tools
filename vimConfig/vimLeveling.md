## 实用命令  
### Level 1--存活:  
```
i → Insert 模式，按 ESC 回到 Normal 模式.
x → 删当前光标所在的一个字符。
:wq → 存盘 + 退出 (:w 存盘, :q 退出)   （陈皓注：:w 后可以跟文件名）
dd → 删除当前行，并把删除的行存到剪贴板里
p → 粘贴剪贴板
推荐:

hjkl (强例推荐使用其移动光标，但不必需) →你也可以使用光标键 (←↓↑→). 注: j 就像下箭头。
:help <command> → 显示相关命令的帮助。你也可以就输入 :help 而不跟命令。（陈皓注：退出帮助需要输入:q）
```
### Level 2--感觉良好:    
1. 各种插入模式  
```
a → 在光标后插入
o → 在当前行后插入一个新行
O → 在当前行前插入一个新行
cw → 替换从光标所在位置后到一个单词结尾的字符
```
Note:  
**cw → 替换从光标所在位置后到一个单词结尾的字符**  

2. 简单的移动光标  
```
0 → 数字零，到行头
^ → 到本行第一个不是blank字符的位置（所谓blank字符就是空格，tab，换行，回车等）
$ → 到本行行尾
g_ → 到本行最后一个不是blank字符的位置。
/pattern → 搜索 pattern 的字符串（陈皓注：如果搜索出多个匹配，可按n键到下一个）
```
Note:  
**g_ → 到本行最后一个不是blank字符的位置。**  

3. 拷贝/粘贴 （陈皓注：p/P都可以，p是表示在当前位置之后，P表示在当前位置之前）  
```
P → 粘贴
yy → 拷贝当前行当行于 ddP
Undo/Redo
u → undo
<C-r> → redo
```
4. 打开/保存/退出/改变文件(Buffer)  
```
:e <path/to/file> → 打开一个文件
:w → 存盘
:saveas <path/to/file> → 另存为 <path/to/file>
:x， ZZ 或 :wq → 保存并退出 (:x 表示仅在需要时保存，ZZ不需要输入冒号并回车)
:q! → 退出不保存 :qa! 强行退出所有的正在编辑的文件，就算别的文件有更改。
:bn 和 :bp → 你可以同时打开很多文件，使用这两个命令来切换下一个或上一个文件。（陈皓注：我喜欢使用:n到下一个文件）
```
Note:  
:x， ZZ 或 :wq → 保存并退出 (:x 表示仅在需要时保存，ZZ不需要输入冒号并回车)  

### Level 3--更好，更强，更快   
**更好**  

下面，让我们看一下vim是怎么重复自己的：  
1. . → (小数点) 可以重复上一次的命令  
2. N<command> → 重复某个命令N次  

- 2dd → 删除2行  
- 3p → 粘贴文本3次  
- 100idesu [ESC] → 会写下 “desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu “  
- . → 重复上一个命令—— 100 “desu “.  
- 3. → 重复 3 次 “desu” (注意：不是 300，你看，VIM多聪明啊).  
**更强**  
你要让你的光标移动更有效率，你一定要了解下面的这些命令，千万别跳过。  
1. NG → 到第 N 行 （陈皓注：注意命令中的G是大写的，另我一般使用 : N 到第N行，如 :137 到第137行）  
2. gg → 到第一行。（陈皓注：相当于1G，或 :1）  
3. G → 到最后一行。  
4. **按单词移动：**   
```
1. w → 到下一个单词的开头。  
2. e → 到下一个单词的结尾。  
```
> 如果你认为单词是由默认方式，那么就用小写的e和w。默认上来说，一个单词由字母，数字和下划线组成（陈皓注：程序变量）  

> 如果你认为单词是由blank字符分隔符，那么你需要使用大写的E和W。（陈皓注：程序语句）  
![wordMoves](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/word_moves.jpg)  

下面，让我来说说最强的光标移动：  
```
% : 匹配括号移动，包括 (, {, [. （陈皓注：你需要把光标先移到括号上）
* 和 #:  匹配光标当前所在的单词，移动光标到下一个（或上一个）匹配单词（*是下一个，#是上一个）]}) (hatcher注：另外一种方法,首先用* 选中当前单词, 然后N移动光标到上一个匹配单词, n移动光标到下一个匹配单词)  
```
**更快**  
你一定要记住光标的移动，因为很多命令都可以和这些移动光标的命令连动。很多命令都可以如下来干：  
```
<start position><command><end position>
```
例如 0y$ 命令意味着：  

- 0 → 先到行头  
- y → 从这里开始拷贝  
- $ → 拷贝到本行最后一个字符  
你可可以输入 ye，从当前位置拷贝到本单词的最后一个字符。  
**你可可以输入 y$，从当前位置拷贝到本行的最后一个字符。**  
你也可以输入 y2/foo 来拷贝2个 “foo” 之间的字符串。  

还有很多时间并不一定你就一定要按y才会拷贝，下面的命令也会被拷贝：  

- d (删除 )  
- v (可视化的选择)  
- gU (变大写)  
- gu (变小写)  
- 等等  
（陈皓注：可视化选择是一个很有意思的命令，你可以先按v，然后移动光标，你就会看到文本被选择，然后，你可能d，也可y，也可以变大写等）  

### Level 4--vim 超能力  
你只需要掌握前面的命令，你就可以很舒服的使用VIM了。但是，现在，我们向你介绍的是VIM杀手级的功能。下面这些功能是我只用vim的原因。  
**在当前行上移动光标: 0 ^ $ f F t T , ;**  
- 0 → 到行头  
- ^ → 到本行的第一个非blank字符  
- $ → 到行尾  
- g_ → 到本行最后一个不是blank字符的位置。  
- fa → 到下一个为a的字符处，你也可以fs到下一个为s的字符。  
- t, → 到逗号前的第一个字符。逗号可以变成其它字符。  
- 3fa → 在当前行查找第三个出现的a。  
- F 和 T → 和 f 和 t 一样，只不过是相反方向。  
![lineMoves](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/line_moves.jpg)  

**还有一个很有用的命令是 dt" → 删除所有的内容，直到遇到双引号—— "。双引号可以换成其它字符。**  
**还有一个很有用的命令是 df" → 删除包括遇到双引号"这之间的所有的内容。双引号可以换成其它字符。**  (hatcher补充)  
**还有一个很有用的命令是 d$ → 删除从当前位置开始到本行结束所有的内容。**  (hatcher补充)  

**还有一个很有用的命令是 yt" → 复制所有的内容，直到遇到双引号—— "。双引号可以换成其它字符。**   (hatcher补充)  
**还有一个很有用的命令是 yf" → 复制包括遇到双引号"这之间的所有的内容。双引号可以换成其它字符。**  (hatcher补充)  
**还有一个很有用的命令是 y$ → 复制从当前位置开始到本行结束所有的内容。**  (hatcher补充)  

**区域选择 <action>a<object> 或 <action>i<object>**  
在visual 模式下，这些命令很强大，其命令格式为:  
```
<action>a<object> 和 <action>i<object>  
```
- action可以是任何的命令，如 d (删除), y (拷贝), v (可以视模式选择)。  
- object 可能是： w 一个单词， W 一个以空格为分隔的单词， s 一个句字， p 一个段落。也可以是一个特别的字符："、 '、 )、 }、 ]。'"  

假设你有一个字符串 (map (+) ("foo")).而光标键在第一个 o 的位置。  
- vi" → 会选择 foo.  
- va" → 会选择 "foo".  
- vi) → 会选择 "foo".  
- va) → 会选择("foo").  
- v2i) → 会选择 map (+) ("foo")  
- v2a) → 会选择 (map (+) ("foo"))  
![textObjects](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/textobjects.png)  

**块操作: <C-v>**  
块操作，典型的操作： `0 <C-v> <C-d> I-- [ESC]`  
- ^ → 到行头    
- <C-v> → 开始块操作  
- <C-d> → 向下移动 (你也可以使用hjkl来移动光标，或是使用%，或是别的)  
- I-- [ESC] → I是插入，插入“--”，按ESC键来为每一行生效。  
![rectAngularBlocks](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/rectangular-blocks.gif)   
在Windows下的vim，你需要使用 <C-q> 而不是 <C-v> ，<C-v> 是拷贝剪贴板  

**自动提示： <C-n> 和 <C-p>**  
在 Insert 模式下，你可以输入一个词的开头，然后按 <C-p>或是<C-n>，自动补齐功能就出现了……  
![autoCompletion](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/completion.gif)  

**宏录制： qa 操作序列 q, @a, @@**(略)  

**可视化选择： v,V,<C-v>**  
前面，我们看到了 <C-v>的示例 （在Windows下应该是<C-q>），我们可以使用 v 和 V(hatcher注: V可以用来做全选)。一但被选好了，你可以做下面的事：  

- J → 把所有的行连接起来（变成一行）  
- < 或 > → 左右缩进  
- = → 自动给缩进 （陈皓注：这个功能相当强大，我太喜欢了）  
![autoIndent](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/autoindent.gif)  

在所有被选择的行后加上点东西：  

- <C-v>(hatcher注：不能用v或V代替, 否则功能无效)   
- 选中相关的行 (可使用 j 或 <C-d> 或是 /pattern 或是 % 等……)  
- $ 到行最后  
- A, 输入字符串，按 ESC。  
![appendToManyLines](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/append-to-many-lines.gif)  

**分屏: :split 和 vsplit.**  
下面是主要的命令，你可以使用VIM的帮助 :help split. 你可以参考本站以前的一篇文章VIM分屏。  

- :split → 创建分屏 (:vsplit创建垂直分屏)  
- <C-w><dir> : dir就是方向，可以是 hjkl 或是 ←↓↑→ 中的一个，其用来切换分屏。  
- <C-w>_ (或 <C-w>|) : 最大化尺寸 (<C-w>| 垂直分屏最大化, <C-w>_ hatcher注:水平分屏最大化)  
- <C-w>+ (或 <C-w>-) : 增加(减少)尺寸  
- <C-w>=  : 将分屏的最大化恢复   

### VIM无插件编程技巧  
#### 浏览代码  
首先，我们先从浏览代码开始。有时候，我们需要看多个文件，所以，传统的做法是，我们开多个tty终端，每个tty里用Vim打开一个文件，然后来回切换。这很没有什么效率。我们希望在一个Vim里打开多个文件，甚至浏览程序目录。  
浏览目录的命令很简单：（你也可以直接vim一个目录）  
`:E`  
注意，是大写。于是，你会看到下面这样的界面：  
![Explorer](https://coolshell.cn/wp-content/uploads/2014/03/Explorer.png)   
(hatcher注：此命令在tmux中失效)  
这个界面中，你可以用 j, k 键上下移动，然后回车，进入一个目录，或是找开一个文件。你可以看到上面有一堆命令：  
- 【 – 】 到上级目录  
- 【D】删除文件（大写）  
- 【R】改文件名（大写）  
- 【s】对文件排序（小写）  
- 【x】执行文件  

当然，打开的文件会把现有已打开的文件给冲掉——也就是说你只看到了一个文件。  
  
如果你要改变当前浏览的目录，或是查看当前浏览的目录，你可以使用和shell一样的命令：  

```
:cd <dir> – 改变当前目录

:pwd  – 查看当前目录
```
### 缓冲区  
其实，你用:E 浏览打开的文件都没有被关闭，这些文件都在缓冲区中。你可以用下面的命令来查看缓冲区：  
```
:ls
```
于是，在你的Vim下，你会看到如下界面：  
![buffer_ls](https://coolshell.cn/wp-content/uploads/2014/03/buffer_ls.png)  
你可以看到Vim打开了四个文件，编号是4，5，6，7，如果你要切换打开的文件，这个时候，你不要按回车（按了也没事，只不过按了就看不到:ls输出的buffer列表了），你可以使用下面的命令切换文件（buffer后面的4表示切到4号文件也就是src/http/ngx_http.c）：  
```
:buffer 4
```
或是：  
```
:buffer src/http/ngx_http.c  
```
注意，  
- 你可以像在Shell中输入命令按Tab键补全一样补全Vim的命令。  
- 也可以用像gdb一样用最前面的几个字符，只要没有冲突。如：buff  

你还可以动用如下命令，快速切换：  
```
:bnext      缩写 :bn
:bprevious   缩写 :bp
:blast  缩写 :bl
:bfirst 缩写 :bf
```
上图中，我们还可以看到5有一个%a，这表示当前文件，相关的标记如下：  
```
– （非活动的缓冲区）  
a （当前被激活缓冲区）  
h （隐藏的缓冲区）  
% （当前的缓冲区）  
# （交换缓冲区）  
= （只读缓冲区）  
+ （已经更改的缓冲区）  
```
### 窗口分屏浏览  
把当前窗口上下分屏，并在下面进行目录浏览：  
```
:He   全称为 :Hexplore  （在下边分屏浏览目录）
```
如果你要在上面，你就在 :He后面加个 !，(hatcher注：跟`:E`很像，而且这个可以用在tmux里面)  
```
:He!  （在上分屏浏览目录）
```
如果你要左右分屏的话，你可以这样：  
```
:Ve 全称为 :Vexplore （在左边分屏间浏览目录，要在右边则是 :Ve!）
```
下图是分别用:He 和 :Ve搞出来的同时看三个文件：  
![splitScreen](https://coolshell.cn/wp-content/uploads/2014/03/WindowsExplorer-900x510.png)  
在分屏间的跳转和切换, 先按Ctrl + W，然后按方向键：h j k l  
### 分屏同步移动  
要让两个分屏中的文件同步移动，很简单，你需要到需要同步移动的两个屏中都输入如下命令（相当于使用“铁锁连环”）：  
(hatcher注：可以同步多个屏幕只需要在多个屏幕中分别输入命令`:set scb`)  
```
:set scb
```
如果你需要解开，那么就输入下面的命令：  
```
:set scb!
```
注：set scb 是 set scrollbind 的简写。  

### Tab页浏览目录  
分屏可能会让你不爽，你可能更喜欢像Chrome这样的分页式的浏览，那么你可以用下面的命令：  
```
:Te  全称是 :Texplorer
```
下图中，你可以看到我用Te命令打开了三页，就在顶端我们可以可以看到有三页，其中第一页Tab上的数字3表示那一页有3个文件。  
![TabExplorer](https://coolshell.cn/wp-content/uploads/2014/03/TabExplorer.png)  
我们要在多个Tabe页中切换，在normal模式下，你可以使用下面三个按键（注意没有冒号）：  
```
gt   – 到下一个页

gT  – 到前一个页

{i} gt   – i是数字，到指定页，比如：5 gt 就是到第5页
```
你可以使用 【:tabm {n}】来切换Tab页。  

gvim应该是：Ctrl+PgDn 和 Ctrl+PgUp 来在各个页中切换。  
如果你想看看你现在打开的窗口和Tab的情况，你可以使用下面的命令：  
```
:tabs
```
于是你可以看到：  
![Tab01](https://coolshell.cn/wp-content/uploads/2014/03/Tab01.png)  

使用如下命令可以关闭tab：（当然，我更喜欢使用传统的:q, :wq来关闭）  
```
:tabclose [i] – 如果后面指定了数字，那就关闭指定页，如果没有就关闭当前页
```
最后提一下，如果你在Shell命令行下，你可以使用 vim 的 -p 参数来用Tab页的方式打开多个文件，比如：  
```
vim -p cool.cpp shell.cpp haoel.cpp
vim -p *.cpp
```
注：如果你想把buffer中的文件全转成tab的话，你可以使用下面的命令  
```
:bufdo tab split
```
## Others
- set paste  
We can paste code from external without messy code  
run command as below:  
`:set paste`  
- code align   
`gg=G`  

### 保存会话  
(未完待续)  

## Reference  
- [简明 VIM 练级攻略](https://coolshell.cn/articles/5426.html)  
- [无插件VIM编程技巧](https://coolshell.cn/articles/11312.html)  
- [将VIM变得简单:如何在VIM中得到你最喜爱的IDE特性](https://coolshell.cn/articles/894.html)  

