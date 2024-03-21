// #include<stdio.h>
// struct node{
// 	int value;
// 	struct node *ptr;
// };
// int main(){
// 	struct node n1,n2,n3;
// 	struct node *head,*temp=NULL;
// 	n1.value=10;
// 	n1.ptr=NULL;
// 	n2.value=20;
// 	n2.ptr=NULL;
// 	n3.value=30;
// 	n3.ptr=NULL;
// 	n1.ptr=&n2;
// 	n2.ptr=&n3;
// 	head=&n1;
// 	temp=head;
// 	struct node n4;
// 	n4.value=100;
// 	n4.ptr=NULL;
// 	n2.ptr=&n4;
// 	n4.ptr=&n3;
// 	// while (head!=NULL){
// 	// 	printf("%d->",head->value);
// 	// 	head=head->ptr;
// 	// 	if (head==NULL){
// 	// 		printf("None");
// 	// 	}
// 	// }
// 	struct node *slow,*fast,*a=NULL;
// 	slow=temp;
// 	fast=temp;
// 	while(fast->value!=100){
// 		slow=fast;
// 		fast=fast->ptr;
// 	}
// 	a=fast->ptr;
// 	fast->ptr=NULL;
// 	slow->ptr=a;
// 	head=temp;
// 	while (head!=NULL){
// 		printf("%d->",head->value);
// 		head=head->ptr;
// 		if (head==NULL){
// 			printf("None");
// 		}
// 	}


// }
#include <stdio.h>

struct node{
  int val;
  struct node *ptr;
};

typedef struct node NODE;

void dispList(NODE *);

int main()
{
  NODE *head = NULL, *temp = NULL;
  NODE *newNode=NULL;
  int ch=1;
  while(ch){
    newNode = (NODE *)malloc(sizeof(NODE));
    printf("\nEnter the new node val: ");
    scanf("%d",&newNode->val);
    newNode->ptr = NULL;
   
    if (head == NULL)
    {
      // empty list
      head = newNode;
      temp = head;
    }
    else{
      // list is present
      head->ptr = newNode;
      head = head->ptr;
    }
   
    printf("\nDo you want to create new node (1/0): ");
    scanf("%d",&ch);
  }
 
  head = temp;
  dispList(head);
 
  return 0;
 
}


void dispList(NODE *head)
{
  printf("\nList is\n");
  while(head)
  {
    printf("%d->",head->val);
    head = head->ptr;
  }
  printf("NULL\n");
}