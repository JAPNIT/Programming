//
//  main.cpp
//  XENTASK
//
//  Created by Japnit Kaur Ahuja on 04/03/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t,n,one=0,two=0,temp;
    cin >> t;
    for(int a0=0; a0<t; a0++)
    {
        cin >> n;

        
        for(int i0=0; i0<n; i0++)
        {
            cin >> temp;
            if(i0%2 == 0)
                one = one + temp;
            else
                two = two + temp;
            
        }
        
        for(int z0=0; z0<n; z0++)
        {
            cin >> temp;
            if(z0%2 == 0)
                two = two + temp;
            else
                one = one + temp;
        }
        
        if (one < two)
            cout << one << endl;
        else
            cout << two << endl;
        
        
        
    }
}
