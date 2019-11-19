
list=[1,3,3234,3902,0]#list可以不同数据类型混用
'''
print(list[:5])
del list[2]#删除了列表中第三个元素
print(list[::-1])
l=len(list)
m=max(list)
print(l)||print(len(list))
print(m)||print(max(list))
'''
list. append(3) #列表后面添加了 括号内函数
print('修改后的列表',list)
print('3的个数：',list.count(3))
list_pop=list.pop(2)#已经删掉了 3234
print('pop删除的数',list_pop)
print(list)#出来结果是 [1,3,3234,3902,0]
'''
pop函数相比较remove函数有返回值，可以知道删掉了的数
'''
list.reverse()#逆序排列列表
print(list)