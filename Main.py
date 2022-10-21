from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        if self.head==None:
            self.head=Node(data)
        else:
            current=self.head
            while(current.next):
                current=current.next
            current.next=Node(data)


    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        self.l=[]
        curr=self.head
        #self.l.append(curr.data)
        #print(curr.data,"(((((")
        while(curr):
            self.l.append(curr.data)
        #    print(curr.data, "(((((((")
            curr=curr.next
        print(self.l)




class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        cur=first_list.head
        a=1
        while(cur.next):
            cur=cur.next
            a+=1

        cur = second_list.head
        b = 1
        while (cur.next):
            cur = cur.next
            b += 1



        while(a<b):
            first_list.insert_at_end(0)
            a+=1
        while(a>b):
            second_list.insert_at_end(0)
            b+=1
        #print("\n\n\n\n\nfirst:", first_list.status(), "\n\n\n\n")
        #print("\n\n\n\n\nsecond:", second_list.status(), "\n\n\n\n")

        fcur=first_list.head
        scur=second_list.head
        ans=LinkedList()
        prev=0
        #print()
        for k in range(a):
            if prev == 1:
                a = fcur.data + scur.data + 1
                prev = 0
                count = 0
                if a >= 10:
                    count = a - 10
                    prev = 1
                    ans.insert_at_end(count)
                    #print(k," ",count,"/////")
                    #ans.status()
                    fcur = fcur.next
                    scur = scur.next
                else:
                    ans.insert_at_end(a)
                    #print(k, " ",a,"****")
                    #ans.status()
                    fcur = fcur.next
                    scur = scur.next

            else:
                a = fcur.data + scur.data
                count = 0
                if a >= 10:
                    count = a - 10
                    prev = 1
                    ans.insert_at_end(count)
                    #print(count," &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                    #print(k, " ", count,"----")
                    #ans.status()
                    fcur = fcur.next
                    scur = scur.next

                else:
                    ans.insert_at_end(fcur.data + scur.data)
                    #print(k, " ", fcur.data + scur.data,"+++++")
                    #ans.status()
                    fcur = fcur.next
                    scur = scur.next
        if(prev==1):
            ans.insert_at_end(1)
        #ans.status()
        return ans








# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
