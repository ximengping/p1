#class C(object):
#  def __init__(self，x=10,y=10):
#     # 构造器
#  self.a=10
#  self.b=20
#
#  def Print(self):
#     #此处变量名是允许使用任何合法的名字的，但是
#      #一般约定俗称的写法就是叫做self
#       print self.a,self.b
#c=C(x=100,y=200)
#c.Print()

##静态方法
#静态方法中无法访问类属性
#class C(object):
#    x=100
#    @staticmethod
#    def Print():
#        print 'hehe'
#        print x
#C.Print()

#类方法（静态成员函数）

class C(object):
    x=100
    @classmethod
    def Print(cls):
        print cls.x
#类自身也是一个type类型的对象
#类方法参数至少会带上一个type类型的实例

c=C()
print id(C)
print type(C)

print id(c)
print type(c)




C.Print()

