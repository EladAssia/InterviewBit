Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1
NOTE : If you are using your own declared glo
 
##########################################################################################################################################

class MinStack:
    # @param x, an integer
    def push(self, x):
        if hasattr(self, 'A'):
            self.A.append(x)
            if len(self.minn) > 0:
                if x < self.minn[-1]:
                    self.minn.append(x)
            else:
                self.minn.append(x)
        else:
            self.A = [x]
            self.minn = [x]
        return self
        
    # @return nothing
    def pop(self):
        if hasattr(self, 'A') and len(self.A) != 0:
            tmp = self.A.pop()
            if tmp == self.minn[-1]:
                self.minn.pop()

    # @return an integer
    def top(self):
        if hasattr(self, 'A'):
            if len(self.A) == 0:
                return -1
            else:
                return self.A[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if hasattr(self, 'A'):
            if len(self.A) == 0:
                return -1
            else:
                return self.minn[-1]
        else:
            return -1

##########################################################################################################################################
