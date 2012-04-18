# -*- coding: utf-8 -*-
"""
題目:

變數 str1 是句文言文，去掉前面的空白後，在'人死為鬼'後面插入英文字母A，並列印出來
輸出應該為"《五音集韻》說：「人死為鬼A，人見懼之；鬼死為魙，鬼見怕之。」  "

提示: 使用str.split或是strings slice notation
"""
str1 = '  《五音集韻》說：「人死為鬼，人見懼之；鬼死為魙，鬼見怕之。」  '
part = str1.strip().split('，人')
print part[0] + 'A，人' + part[1]

