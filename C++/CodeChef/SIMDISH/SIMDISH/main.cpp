//
//  main.cpp
//  SIMDISH
//
//  Created by Japnit Kaur Ahuja on 07/04/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t,count;
    cin >> t;
    for(int t0=0; t0<t; t0++)
    {
        count = 0;
        string one[4], two[4],ans;
        
        for(int j0=0; j0<4; j0++)
            cin >> one[j0];
        for(int j0=0; j0<4; j0++)
            cin >> two[j0];
        
        for(int j0=0; j0<4; j0++)
            for(int h0=0; h0<4; h0++)
            {
                if(count == 2)
                    break;
               
                if(one[j0] == two[h0])
                    count++;
                    
            }
        if(count >= 2)
            cout << "similar" << endl;
        else
            cout << "dissimilar" << endl;
        
        
    }
}
