# soraha_utils
## 这是什么?
羽衣从杂物箱里翻出来的乱七八糟的工具们,但现在已经把这项轻松工作丢给精灵们了,真的很懒呢！
## 内容
- 此处仅介绍拥有的功能,具体使用请查阅函数注释
- 装饰器sync_with_hook|async_with_hook: 对hook功能的简单实现,可以做到优先调用预处理A函数->注册的特定函数->结束B函数
- uilog: 对loguru的再次封装,改成了自己常用的样子
- sync_uio|async_uio:尝试性的对文件处理的不同方法统一为一个函数,可以传递url保存json/图片,或者传递数据保存json/任意文本/图片
- uiclient: 同上,尝试性的将自己各种项目的重复网络请求代码统一,增加了统一的log输出以及uitry的功能,同步基于requests,异步基于httpx
- uitry: 简单的重试函数的实现
- sync_to_async: 懂的都懂(……?)
## 为什么要写这个
- 重复的代码太多了呜呜呜,大家都有轮子,我也得造一个
## 未来期望
* [ ] 会逐渐把所有重复率高的代码加进去
* [ ] 因为常用nonebot,可能加入相关内容,也可能单独开个wheel
* [ ] 尝试将自己项目中相对好用的功能提取出来(例如搜图搜本功能)
## 更新日志
### 0.0.17 (2022/2/11)
- 修复
  - 全体目光向我看齐，我宣布个事，我……(总之就是很弱智的bug！)
### 0.0.16 (2022/2/11)
- 优化
  - 简单整理了一下文件结构,再也不用一堆乱七八糟的py文件堆在一个文件夹啦
  - 更改了一下readme文件使其更简洁(有吗?)
### 0.0.15 (2021/12/2)
- 修复retry重复的问题
- 新增exception: Uitry_END_Trying
  - 用于抛出以主动跳出uitry
> 诶?为什么0.0.10~0.0.14的更新日志没写?忘光了……
### 0.0.9 (2021/11/2)
- 修复由于打错字导致的bug(逃
### 0.0.8 (2021/10/20)
- 修复uiclient的相关问题(headers加入过多无意义内容导致返回出现问题)
### 0.0.7 (2021/10/19)
- 简化uio的save_file,减少了重复代码,用pathlib替代os.path

## LICENSE!
请给我钱 License  
版权所有(c) 2021 shiying  
1. 任何人都可以使用、复制、修改、合并、发布、分发本软件的副本
2. 用于商业化或修改后需要闭源请征得作者同意
3. 禁止单独将该软件的副本出售
4. 本软件不包含任何形式的明示或暗示
5. 作者不对本软件的任何第三方修改版负责
6. 作者对软件的可用性及稳定性不做任何保证(但应该会持续更新且debug！)
7. 作者不清楚这个软件在干嘛,但是作者很可爱
8. 由上：请给作者PR或issue！谢谢
9. 祝你好运
10. 大家一起开心的掉头发吧！