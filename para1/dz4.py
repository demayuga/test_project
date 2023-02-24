class BaseClass1:
    def __init__(self):
        self.base_attr1 = 'Base Attribute 1'


    def base_method1(self):
        print('Base Method 1')


class BaseClass2:
    def __init__(self):
        self.base_attr2 = 'Base Attribute 2'


    def base_method2(self):
        print('Base Method 2')


class SubClass(BaseClass1, BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)
        self.sub_attr = 'Sub Attribute'


    def sub_method(self):
        print('Sub Method')


sub = SubClass()
print(sub.base_attr1)
print(sub.base_attr2)
sub.base_method1()
sub.base_method2()
print(sub.sub_attr)
sub.sub_method()