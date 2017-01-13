//
//  main.cpp
//  Topic:Graphs
//
//  Created by Japnit Kaur Ahuja on 13/01/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>

using namespace std;

struct Node_adj_list // making node of adjacency list
{
    int dest; // index of the node its connected to
    int cost; // cost of going to one node to another, if any
    Node_adj_list* next;
    
};

struct adj_list// head ptr to the adjacency list
{
    Node_adj_list* head;
};

struct graph
{
    int v;
    adj_list* array;
    
};

Node_adj_list* new_node(int dest,int cost) // helper function to create a node
{
    Node_adj_list* new_node = new Node_adj_list;
    new_node -> dest = dest;
    new_node -> cost = cost;
    new_node -> next = NULL;
    return new_node;
}

graph* create_graph(int v)
{
    graph* Graph = new graph;
    Graph -> v = v;
    Graph -> array = new adj_list[v] ;
    
    for (int i=0; i<v; i++)
    {
        Graph -> array[i].head = NULL;
        
    }
    
    return Graph;
    
}

void addEdge(graph* Graph , int src, int dest,int cost )
{
    Node_adj_list* temp = new_node(dest,cost); // creating a new node
    temp -> next = Graph->array[src].head; // setting up the links
    Graph->array[src].head = temp;
    
    //if an undirected graph, then add opposite link too
    
    Node_adj_list* temp1 = new_node(src,cost);
    temp1 -> next = Graph->array[dest].head;
    Graph->array[dest].head = temp1;
    
    
}

void print(graph* Graph)
{
    int v= Graph->v;
    for(int i=0;i<v;i++)
    {
        Node_adj_list* crawl = Graph->array[i].head;
        cout << "connections of " << i << endl;
        while(crawl)
        {
            cout << crawl->dest << " " << crawl->cost << endl;
            crawl = crawl->next;
        }
    }
}

int main()
{
    int V = 5;
    graph* Graph = create_graph(V);
    addEdge(Graph,0,1,100);
    addEdge(Graph,0,4,10);
    addEdge(Graph,1,2,30);
    addEdge(Graph,1,3,40);
    addEdge(Graph,1,4,70);
    addEdge(Graph,2,3,80);
    addEdge(Graph,3,4,10);
    print(Graph);

    
}
