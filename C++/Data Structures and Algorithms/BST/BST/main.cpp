//
//  main.cpp
//  Data_structure
//  topic : binary search trees
//  Created by Japnit Kaur Ahuja on 07/01/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

struct Node // tree data structure
{
    int data;
    Node* left;
    Node* right;
    
};
Node* root = NULL;

Node* insert (Node* pointer, int x); // inserts data
Node* New_node(int data); // helper for insert, makes a new node and returns a pointer of that node
bool search(Node* pointer, int x); // searches for a vlaue, returns true or false
int max(Node* pointer); // max val in the tree - recursively
int min(Node* pointer); // min val in the tree - iteratively
int find_height(Node* pointer); // finds the height of the tree
bool is_binary_search_tree(Node* pointer); // checks if a tree is a binary search tree or not
bool binary_search_tree_helper(Node* pointer, int min, int max);
// BST is when all individual nodes are also BST
Node* Delete(Node* pointer, int x); // deleting a node


int main()
{
    // insert , search , max , min , hieght
    root = insert(root, 50); // first root should be initialised
    insert(root, 30);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    Delete(root,30);
    Delete(root,70);
    cout << "maximum:" << max(root) << endl;
    cout << "minimum:" << min(root) << endl;
    cout << "height:" << find_height(root) << endl;
    cout << "is BST?:" << is_binary_search_tree(root) << endl;
    return 0;
}

Node* insert(Node* pointer, int x)
{
    if (pointer == NULL) return New_node(x); //traverses the list till finds a place to insert

    if (x < pointer->data)
        pointer->left  = insert(pointer->left, x);
    else if (x > pointer->data)
        pointer->right = insert(pointer->right, x);
    return pointer;
}

Node* New_node(int data)
{
    Node* temp = new Node(); // makes a new node
    temp -> data = data;
    temp -> left = NULL;
    temp -> right = NULL;
    return temp;
}

bool search(Node* pointer, int x)
{
    if (pointer == NULL)
        return false;
 
    else if (x == pointer-> data)
        return true;
    
    else if (x<= pointer-> data) // searches the whole tree cutting half each time
        return search(pointer->left,x);
    
    else // binary search
        return search(pointer->right,x);
   
}

int max(Node* pointer)
{
    if (pointer == NULL)
        return -1;
    if (pointer->right == NULL) // tranverses till the right-most node
        return pointer->data;
    return max(pointer->right);
    
}

int min(Node* pointer)
{
    if (pointer == NULL)
        return -1;
    while (pointer->left != NULL) // traverses till the left-most node
        pointer = pointer->left;
    return pointer->data;
    
}

int find_height(Node* pointer)
{
    if (pointer==NULL)
        return 0;
    return max(find_height(pointer -> right) , find_height(pointer->left)) +1;
    
}

bool is_binary_search_tree(Node* pointer)
{
    return binary_search_tree_helper(pointer,INT_MIN,INT_MAX);
}


bool binary_search_tree_helper(Node* pointer,int min, int max)
{
    if (pointer == NULL)
        return true;
    if (pointer->data > min && // setting a range for each node, the max and min that it could be
        pointer->data<max &&
        binary_search_tree_helper(pointer->left, INT_MIN, pointer->data) &&
        binary_search_tree_helper(pointer->right, pointer->data, INT_MAX))
        return true;
    return false;
    
}
Node* Delete(Node* pointer, int x)
{
    if (pointer == NULL)
        return pointer;
    else if (pointer->data > x)
        pointer->left = Delete(pointer->left,x);
    else if (pointer->data < x)
        pointer->right = Delete(pointer->right,x);
    else
    {
        //Case 1 -> 0 child
        if (pointer->left == NULL && pointer->right == NULL)
        {
            delete pointer;
            pointer = NULL;
        }
        //Case 2 -> 1 child
        else if (pointer->left == NULL)
        {
            Node* temp = pointer;
            pointer = pointer -> right;
            delete temp;
        }
        
        else if (pointer->right == NULL)
        {
            Node* temp = pointer;
            pointer = pointer->left;
            delete temp;
        }
        //Case 3 -> 2 children
        else
        {
            pointer->data = min(pointer->right);
            pointer->right = Delete(pointer->right,pointer->data);
            
        }
        
        
    }
    return pointer;
}
