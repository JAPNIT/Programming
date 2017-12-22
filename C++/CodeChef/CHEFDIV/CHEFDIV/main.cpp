//
//  main.cpp
//  CHEFDIV
//
//  Created by Japnit Kaur Ahuja on 13/04/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <map>
#include <cmath>
using namespace std;

int main()
{
    int a,b,total = 0,max,no_div,y,ans=0;
    cin >> a >> b;

    // check for number 50
    for(int n=a; n<=b; n++)
    {
        total = 0;
        max = n;
        no_div = 1;
        
        for(int n0 = 2; n0 <= pow(max,.5); n0++)
        {
            if( max == 2)
                break;
            if( max % n0 == 0)
                no_div = no_div + 2;
            if(n0 == pow(max,.5))
                no_div = no_div - 1;
        }
        
        while(no_div != 1)
        {
            
            total = total + no_div + 1;

        
            for(int h0 = 2; h0 <= pow(max,.5); h0++)
            {
                if (max % 2 == 0 && max % h0 == 0)
                {
                        y = max / h0;
                        
                        if(y%2==0)
                        {
                            max = y;
                            break;
                        }
                    
                }
                
                if(max % h0 == 0 && max % 2 != 0)
                {
                    y = max / h0;
                    max = y;
                    break;
                    
                }
                
                if(max % h0 == 0)
                {
                    y = max / h0;
                    max = y;
                    break;
                }
            }
            
            no_div = 1;
            for(int n0 = 2; n0 <= pow(max,.5); n0++)
            {
                if( max % n0 == 0)
                    no_div = no_div + 2;
                if(n0 == pow(max,.5))
                    no_div = no_div - 1;
            }
            
            if(no_div == 1)
                total = total + 3;

            
            
        }
        
        if(total == 0)
            total = total + 2;
        else
            total = total -1;
        ans = ans + total;
        
        
    
    }

    cout << ans << endl;
}
