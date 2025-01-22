# Below are examples of "Method Chaining":

class A:
    def m1(self):
        return 'hello from class A'
    
class B(A):
    def m1(self):
        return 'hello from class B'
    
class C(B):
    def m1(self):
        return 'hello from class C'
    
if __name__ == '__main__':
    c = C()
    print(c.m1())
    
