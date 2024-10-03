#CLL-IMPLENTATION & INSERTION
class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class CLL:
    def _init_(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode =node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
    def display(self):
        self.temp=self.head
        while self.temp.next!=self.head:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print(self.temp.data)
        print()
    def insert_at_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        self.tail.next=self.head
    def insert_at_end(self,data):
        newnode=node(data)
        self.tail.next=newnode
        newnode.next=self.head
    def insert_at_mid(self,data,pos):
        newnode=node(data)
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
        newnode.next=self.temp.next
        self.temp.next=newnode
obj=CLL()
while(1):
    print("1.create 2.display 3.insert_at_front 4.insert_at_mid 5.insert_at_end")
    choice=int(input("enter the choice"))
    if choice==1:
        data=int(input("enter the data"))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        data=int(input("Enter the data"))
        obj.insert_at_front(data)
    elif choice==4:
        data=int(input("enter the data"))
        pos=int(input("enter the pos"))
        obj.insert_at_mid(data,pos)
    elif choice==5:
        data=int(input("enter the data"))
        obj.insert_at_end(data)
