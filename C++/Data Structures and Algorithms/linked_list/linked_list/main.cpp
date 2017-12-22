//
//  main.cpp
//  Data_structure
//  topic : linked lists
//  Created by Japnit Kaur Ahuja on 05/01/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct Node // creating a new data structure
{
    int data;
    Node* next; // pointer to the next node
};

Node* head;

void insert(int x, int n) // inserting a node where data is x at position n (stars from 0)
{
    try
    {
        Node* temp1 = new Node(); // creation of a new node
        temp1 -> data = x; // addition of the data
        if (head == NULL || n==0)
        {
            temp1 -> next = head; // temp -> next = NULL
            head = temp1; // head now points to temp1
        }
        
        else
        {
            Node* temp2 = head;
            for (int y=0; y<n-1; y++) // loop till the (n-1)th node
            {
                temp2 = temp2 -> next;
                
            }
            temp1 -> next = temp2 -> next; // nth node points at the (n+1)th node
            temp2 -> next = temp1; // (n-1)th node points at the nth node
            
        }
        
    }
    catch (...)
    {
        cout << " Not a valid position" << endl;
    }
    
    
}

void Delete(int n)
{
    Node* temp1 = head; // temp1 is a pointer to head which is the pointer to NULL or the first node
    if (n==0)
    {
        head = temp1 -> next; // head points to (n+1)th node
        delete temp1; // deleting nth node
        return;
    }
    for(int p=0; p<n-1; p++)
        temp1 = temp1 -> next; // temp1 points to the (n-1)th node
    Node* temp2 = temp1 -> next; // temp2 points to (n)th node
    temp1 -> next = temp2 -> next; // now the (n-1)th node points to the (n+1)th node
    delete temp2; // deleting the nth node
    
    
}
void print()
{
    Node* temp = head; // temp points to NULL or the first node
    if (temp == NULL)
    {
        cout << "empty list" << endl;
    }
    else
    {
        while (temp != NULL)
        {
            int a = temp -> data;
            cout << a << " ";
            temp = temp -> next; //temp keeps on going to the next node till the last nod epointd to NULL
        }
        
        cout << endl; // just for beautification purposes ;p
    }
    
}

void reverse()
{
    Node* current = head; // points to the current node
    Node* prev = NULL; // points to the previous node, and the previous node for the 1st node is NULL
    Node* following; // points to the next node
    while (current != NULL)
    {
        following = current -> next; // following saves the value of next node
        current -> next = prev; // as the current node's link is going to be changes to the prvious node
        prev = current; // now the previous node equals the current node
        current = following; // the current moves onto the next node
        
    }
    head = prev;
    
}

void print_recur(Node* pointer)
{
    if (pointer == NULL) // goes till the end
    {
        return;
    }
    int a = pointer -> data;
    cout << a << " " ; // prints then moves on
    print_recur(pointer -> next);
}

void print_reverse_recur(Node* pointer)
{
    if (pointer == NULL) // goes till the end node
    {
        return;
    }
    print_reverse_recur(pointer -> next); // first goes till the end, then prints in the reverse order
    int a = pointer -> data;
    cout << a << " " ;
    
}


int main()
{
    head = NULL;
    // call insert , Delete , print , reverse , print_recur , print_reverse_recur
       
    insert(4,1);
    insert(2,0);
    insert(3,2);
    insert(18,3);
    insert(8,4);
    
    reverse();

    print_recur(head);
}

