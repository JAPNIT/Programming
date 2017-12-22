//
//  main.cpp
//  Topic:Graphs
//
//  Created by Japnit Kaur Ahuja on 13/01/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <string>
#include <list>

using namespace std;

struct Node_adj_list // making node of adjacency list
{
    int dest; // index of the node its connected to
    int cost; // cost of going to one node to another, if any
    Node_adj_list* next;
    bool visited = false;
    
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
        Node_adj_list* temp = Graph -> array[src].head;
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
                temp = temp->next;
            }
        }
        
    }
    return false;
    
}

void Djikstra_Shortest_Path(graph* Graph ,int n)// shortest path from the 0 node
{
    int shortest_dist[n],count = 0;
    bool visited[n];
    
    for (int k0=0; k0<n; k0++)
    {
        shortest_dist[k0] = INT_MAX;
        visited[k0] = false;
    }
    
    shortest_dist[0] = 0;
    int min = 0;
    
    while(count <= n)
    {
        int min_val = INT_MAX;
        for (int g0=0; g0<n; g0++)
        {
            if (visited[g0] == false && shortest_dist[g0]<= min_val)
            {
                min_val = shortest_dist[g0];
                min = g0;
            }
            
            
        }

        visited[min] = true;
        count++;
        
        Node_adj_list* temp = Graph->array[min].head;
        
        int dist_till_min = shortest_dist[min];
        
        while(temp != NULL)
        {
            int distance =  dist_till_min + temp->cost;
            if (visited[temp->dest] == false && distance < shortest_dist[temp->dest])
                shortest_dist[temp->dest] = distance;
            temp = temp->next;
        }
    }
    
    for (int k0 = 0; k0<n; k0++)
    {
        cout << shortest_dist[k0] << endl;
    }
            
    
}

int main()
{
    int n = 9;
    graph* graph = create_graph(n);
    addEdge(graph, 0, 1, 4);
    addEdge(graph, 0, 7, 8);
    addEdge(graph, 1, 2, 8);
    addEdge(graph, 1, 7, 11);
    addEdge(graph, 2, 3, 7);
    addEdge(graph, 2, 8, 2);
    addEdge(graph, 2, 5, 4);
    addEdge(graph, 3, 4, 9);
    addEdge(graph, 3, 5, 14);
    addEdge(graph, 4, 5, 10);
    addEdge(graph, 5, 6, 2);
    addEdge(graph, 6, 7, 1);
    addEdge(graph, 6, 8, 6);
    addEdge(graph, 7, 8, 7);
    
    Djikstra_Shortest_Path(graph,n);
    

    

    
}
