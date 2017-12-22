//
//  main.cpp
//  BRLADDER
//
//  Created by Japnit Kaur Ahuja on 30/03/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{
    int q,i,temp;
    cin >> q;
    for(int h0=0; h0<q; h0++)
    {
        int a,b;
        cin >> a >> b;
        
        if (b<a)
        {
            temp = a;
            a = b;
            b = temp;
        }

        
        if(b-a == 2)
            cout << "YES" << endl;
         else
         {
                 
             i= (a-1) / 2;

             if (b == (2*i) + 2)
                 cout << "YES" << endl;
             else
                 cout << "NO" << endl;
             
         }
    }
}

