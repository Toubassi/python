class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
  
  def add_to_start(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = self.new_node
      return self
    new_node = self.head
    self.head = new_node

  def add_to_end(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      return self
    current = self.head
    while current.next != None:
      current = current.next
    current.next = new_node


LinkedList.add_to_start(5)
