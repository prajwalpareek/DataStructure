class Node:
    def __init__(self,data=None,Next=None):
        self.data = data
        self.Next = Next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beg(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data,self.head)
            self.head = new_node
            
    def Display(self):
        itr = self.head
        while itr:
            print(itr.data, end = " ")
            itr = itr.Next
            
    def get_length(self):
        itr = self.head
        count = 1
        while itr:
            itr = itr.Next
            count += 1
        return count    
            
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data)
        else:    
            itr = self.head
            while itr.Next!=None:
                itr = itr.Next
            itr.Next = Node(data)
            
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            print("index out of range")
        
        elif self.head == None:
            self.head = Node(data)
        else:
            ind = 0
            itr = self.head
            while ind<index:
                if ind==index-1:
                    new_node = Node(data,itr.Next)
                    itr.Next = new_node
                    break
                itr = itr.Next
                ind += 1 
    
    def Delete_at(self,index):
        if index<0 or index>self.get_length():
            print("index out of range")
        else:
            itr = self.head
            ind = 0
            while ind<index:
                if ind == index-1:
                    itr.Next = itr.Next.Next
                itr = itr.Next
                ind += 1
    
    def many_elements(self,li):
        self.head = None
        for item in li:
            self.insert_at_end(item)
            
            
if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_end(10)
    obj.insert_at_end(20)
    obj.insert_at_end(30)
    obj.insert_at_end(40)
    obj.insert_at_end(50)
    obj.insert_at(4,99)
    obj.Delete_at(3)
    # li = [2,5,8,13]
    # obj.many_elements(li)
    obj.Display()