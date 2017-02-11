//
//  main.cpp
//  Travel_Agency
//  https://www.hackerrank.com/contests/exun-programming-finals/challenges/tourist-agency
//  Created by Japnit Kaur Ahuja on 13/01/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <string>
#include <list>

using namespace std;

struct Node // graph nodes
{
    int dest;
    Node* next;
};

struct adj_head // head ptr to graph nodes
{
    Node* head;
};

struct graph // basic structure of a graph
{
    int vertices;
    adj_head* array;
};

Node* new_node(int dest) // creates new node
{
    Node* new_node = new Node;
    new_node -> dest = dest;
    new_node -> next = NULL;
    return new_node;
}

graph* create_graph(int v) // creates a new graph
{
    graph* Graph = new graph;
    Graph->vertices = v;
    Graph->array = new adj_head[v];
    
    for(int x0=0; x0<v; x0++)
    {
        Graph->array[x0].head = NULL;
    }
    
    return Graph;
    
    
}

void add_edge(graph* Graph,int a, int b)
{
    Node* temp1 = new_node(b);
    temp1 -> next = Graph->array[a].head;
    Graph->array[a].head = temp1;
    
    temp1 = new_node(a);
    temp1 -> next = Graph->array[b].head;
    Graph->array[b].head = temp1;
    
}

bool BFS(graph* Graph, int src, int dest, int n)
{
    bool visited[n];
    for (int f0=0; f0<n; f0++)
        visited[f0] = false;
    
    list <int> queue;
    
    queue.push_back(src);
    visited[src] = true;
    
   
    while(!queue.empty())
    {
        src = queue.front();
        Node* temp = Graph -> array[src].head;
        queue.pop_front();
        
        if (src == dest)
            return true;
        
        else
        {
            while (temp != NULL)
            {
                if(visited[temp->dest] == false)
                {
                    queue.push_back(temp->dest);
                    visited[temp->dest] = true;
                    
                }
                temp = temp -> next;
            }
        }
        
    }
    return false;
   
}


bool bridge(graph* Graph,int a, int b,int n)
{
    if(BFS(Graph,a,b,n) == false)
        return true;
    return false;
}

/*int excursion(graph* Graph, int src, int dest, int n , int penguins[])
{
    bool visited[n];
    for (int f0=0; f0<n; f0++)
        visited[f0] = false;
    
    list <int> queue;
    
    queue.push_back(src);
    visited[src] = true;
    
    int answer = 0;
    
    
    while(!queue.empty())
    {
        src = queue.front();
        Node* temp = Graph -> array[src].head;
        queue.pop_front();
        
        if (src == dest)
        {
            answer = 1;
            break;
        }
        
        
        else
        {
            while (temp != NULL)
            {
                if(visited[temp->dest] == false)
                {
                    queue.push_back(temp->dest);
                    visited[temp->dest] = true;
                    
                }
                temp = temp -> next;
            }
        }
        
    }
    
    if (answer == 1)
    {
        answer = 0;
        for (int f0=0; f0<n; f0++)
            if (visited[f0] == true)
            {
                int temp = penguins[f0];
                cout << "adding " << temp << endl;
                answer = answer + temp;
            }
        
        
    }
    return answer;
    
} */

int main()
{
    int n;
    cin >> n;
    int penguins[n];
    graph* Graph = create_graph(n);
    
    for(int a0=0; a0<n; a0++)
    {
        cin >> penguins[a0];
    }
    
    int q;
    cin >> q;
    
    for(int y0=0; y0<q; y0++)
    {
        string command;
        int a,b;
        cin >> command >> a >> b;
        a = a-1;
        // till now taking input, now the program starts
        
        if(command == "penguins")
        {
            penguins[a] = b;
        }
        
        else if(command == "bridge")
        {
            if(bridge(Graph,a,b,n))
            {
                cout << "yes" << endl;
                add_edge(Graph,a,b);
            }
            
            else
                cout << "no" << endl;
        }
        
        /* penguin code left else
        {
            //int ex = excursion(Graph,a,b,n,penguins);
            if(0) //excursion(a,b)
            {
                cout << "total number of penguins through djiktras shortest path algo" << endl;
                
            }
            
            else
                cout << "impossible" << endl;
        }
        
        
        */
    }
    
}
