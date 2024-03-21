import java.util.*;
public class LL{
	static Node head;
	LL(){
		this.head=null;
	}
	static void insertEnd(int data){
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
	static void insertFirst(int value){
		Node newNode=new Node(value);
		if (head==null){
			head=newNode;
		}
		else{
			newNode.next=head;
			head=newNode;
		}
	}
	static void display(){
		Node ptr=head;
		while(ptr!=null){
			System.out.print(ptr.data+"->");
			ptr=ptr.next;
			if (ptr==null){
				System.out.print("None");
			}
		}
	}
	public static void main(String args[]){
		LL list=new LL();
		list.insertEnd(10);
		list.insertEnd(20);
		list.display();

	}
}
class Node{
	int data;
	Node next;
	Node(int data){
		this.data=data;
		this.next=null;
	}
}