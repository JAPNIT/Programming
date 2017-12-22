//
//  main.cpp
//  Tidy Numbers
//
//  Created by Japnit Kaur Ahuja on 08/04/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

bool tidy(long long n)
{
    while(n != 0)
    {
        int last = n%10;
        n = n/10;
        if (n%10 > last)
            return false;
    }
    
    return true;

    
}
int main()
{
    ifstream x ("/Users/Japnit/Desktop/Tidy Numbers/input1.txt");
    ofstream y ("/Users/Japnit/Desktop/Tidy Numbers/output1.txt");
    
    int t;
    long long n;

    x >> t;
    for(int h0=0; h0<t; h0++)
    {
         x >> n;

        for(long long j0=n; j0>0; j0--)
        {
            if(tidy(j0))
            {
                n = j0;
                break;
            }

        }
        
        y << "Case #" << h0+1 << ": " << n<< endl;

    
        
    }
    
    x.close();
    y.close();
    

}
