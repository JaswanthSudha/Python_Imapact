class Node{
    int data;
    Node next;
    Node(int data){
        this.data=data;
        this.next=null; 
    }
}
class LinkedList{
    static Node head;
    LinkedList(){
        this.head=null;
    }
    public static void insert(int data){
        Node newNode=new Node(data);
        if (head==null){
            head=newNode;
        }
        else{
            Node ptr=head;
            while(ptr.next!=null){
                ptr=ptr.next;
            }
            ptr.next=newNode;
        }
    }
    public static void printF(){
        Node ptr=head;
        while(ptr!=null){
            System.out.print(ptr.data+"->");
            ptr=ptr.next;
        }
        System.out.print("End");
    }
    public static void main(String args[]){
       LinkedList ll=new LinkedList();
       ll.insert(10);
       ll.insert(20);
       ll.insert(30);
       ll.insert(40);
       ll.printF();
    }
}