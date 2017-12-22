//
//  main.cpp
//  SUMDIS
//
//  Created by Japnit Kaur Ahuja on 04/03/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <limits>
using namespace std;

struct Node
{
    Node* next;
    int w;
    int dest;
    
};

struct adj_list
{
    Node* head;
};

struct Graph
{
    int v;
    adj_list* array;
};

Node* new_node(int i)
{
    Node* temp = new Node;
    temp -> dest = i;
    temp -> next = NULL;
    
    return temp;
    
}

Graph* Create_graph(int v)
{
    Graph* temp = new Graph;
    temp -> v = v;
    temp -> array = new adj_list[v];
    
    for(int a0=0; a0<v; a0++)
        temp -> array[a0].head = NULL;
    return temp;
    
}



void addEdge(Graph* graph, int src, int dest, int weight)
{
    Node* temp = new_node(dest);
    temp -> next = graph -> array[src].head;
    graph -> array[src].head = temp;
    temp -> w = weight;
    
}



int shortest_dist(Graph* graph,int n,int src,int dest)
{
    int shortest_dist[n],count = 0;
    bool visited[n];
    
    for (int k0=0; k0<n; k0++)
    {
        shortest_dist[k0] = numeric_limits <int>:: max();
        visited[k0] = false;
    }
    
    shortest_dist[src] = 0;
    int min = src;
    
    while(count <= n)
    {
            
        int min_val = numeric_limits <int>:: max();
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
        
        Node* temp = graph->array[min].head;
        
        int dist_till_min = shortest_dist[min];
        
        while(temp != NULL)
        {
            int distance =  dist_till_min + temp -> w;
            if (visited[temp->dest] == false && distance < shortest_dist[temp->dest])
                shortest_dist[temp->dest] = distance;
            temp = temp->next;
        }
    }
    
    return shortest_dist[dest];



    
}



int main()
{
 
    int t0,n,w,temp,total=0;
    cin >> t0;
    
    for(int y0=0; y0<t0; t0++)
    {
        cin >> n;
        total = 0;
        Graph* graph = Create_graph(n-1);
        for(int n0=0; n0<=n-2; n0++)
        {
            cin >> w;
            addEdge(graph,n0, n0+1,w);
            
        }
        
        for(int n0=0; n0<=n-3; n0++)
        {
            cin >> w;
            addEdge(graph,n0, n0+2,w);
            
        }
        
        for(int n0=0; n0<=n-4; n0++)
        {
            cin >> w;
            addEdge(graph,n0,n0+3,w);
            
        }
        
        for(int y0=0; y0<n; y0++)
        {
            for(int n0=0;n0<n;n0++)
            {
                if(y0<n0)
                {
                    temp = shortest_dist(graph,n, y0, n0);
                    total = total + temp;
                    
                }
            }
        }
        
        cout << total << endl;


    }
    
    return 0;
    
    
    
    
}
