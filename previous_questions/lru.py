

# 
# Your previous Java content is preserved below:
# 
# import java.io.*;
# import java.util.*;
# 
# /*
#  * To execute Java, please define "static void main" on a class
#  * named Solution.
#  *
#  * If you need more classes, simply define them inline.
#  */
# 
# 
# 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
        
class LRUcache:
    def __init__(self, size):
        self.size = size
        self.dic = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head
        
        
        
    def get(self, key):
        if key in self.dic:
            curr = self.dic[key]
            self.remove(curr)
            self.add(curr)
            
            return curr.value
        
    def set(self, key, data):
        if key in self.dic:
            del self.dic[key]
            
        new = Node(key, data)
        self.add(new)
        self.dic[key] = new
        # if over size
        if self.size < len(self.dic):
            curr = self.head.next
            self.remove(curr)
            del self.dic[curr.key]
        
        
    def remove(self, node):
        """skip over a node and update prev"""
        temp = node.prev
        temp2 = node.next
        temp2.next = temp2
        temp2.prev = temp
        
        
    def add(self, node):
        """add to back"""
        temp = self.tail.prev
        temp.next = node
        self.tail.prev = node
        node.prev = temp
        node.next = self.tail
        
    def printList(self):
        node = self.head
        while node.next:
            print node.value
            node = node.next
            
        return
        
        

if __name__ == '__main__':
    cache = LRUcache(5)
    
    cache.set('a', 10)
    cache.set('b', 5)
    cache.set('c', 3)
    cache.set('d', 1)
    cache.set('e', 0)
    cache.set('f', 100)
    
    
    cache.printList()
    # print cache.get('b')
    # print cache.get('c')
    # print cache.get('d')
    # print cache.get('e')
    # print cache.get('f')
    # print cache.get('b')
    
    
    
    
    
    
        
    