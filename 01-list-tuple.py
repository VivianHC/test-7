import random
print('\n---cutting line(1)---')
list1=['张飞','赵云','马超','吕布']
tupe1=("刘备","曹操","孙权")
print('\n---cutting line(2)---')
pos=0
value=list1[pos]
print("取出列表的第 %d 个值，它是 %s" % (pos,value))
print("---输出列表中所有元素---")
pos=0
for v in list1:
    print("取出列表的第 %d 个值，它是 %s" % (pos,v))
    pos=pos+1
print('\n---cutting line(4)---')
newvalue='关羽'
list1[0]=newvalue
print("---输出更新后列表中所有元素---")
pos=0
for v in list1:
    print("取出列表的第 %d 个值，它是 %s" % (pos,v))
    pos=pos+1

print('\n---cutting line(5)---')
for i in range(1,5):
    s=random.choice(list1)
    print(s)
print('\n---cutting line(5)---')
for i in range(1,5):
    s=random.choice(tupe1)
    print(s)
