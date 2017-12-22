//
//  main.cpp
//  DGTCNT
//
//  Created by Japnit Kaur Ahuja on 16/04/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int q0=0; q0<t; q0++)
    {
        long long a,b,count = 0;
        int x[10],dig;
        cin >> a >> b;
        for(int y0=0; y0<10; y0++)
            cin >> x[y0];
        
        for(long long n=a; n<=b; n++)
        {
            cout << n << endl;
            int y[10] = {0,0,0,0,0,0,0,0,0,0};
            long long num = n;
            while(num != 0)
            {
                dig = num%10;
                y[dig] = y[dig] + 1;
                num = num/10;
            }
            
            count = count + 1;
            for(int j0=0; j0<10; j0++)
                if(y[j0] == x[j0])
                {
                    count = count - 1;
                    break;
                }
            
        }
        
        cout << count << endl;
 
        
    }


}
