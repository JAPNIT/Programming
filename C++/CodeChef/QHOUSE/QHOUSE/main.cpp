//
//  main.cpp
//  QHOUSE
//
//  Created by Japnit Kaur Ahuja on 02/03/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int high=1000,low=0,guess;
    string i;
    
    
    while(1)
    {
        
        guess = (high + low) / 2;
        cout << "?" << " " << guess << " " << 0 << flush;
        cin >> i;
        
        if (abs(high - low) == 1)
            break;
        
        if (i == "YES")
            low = guess;
        else
            high = guess;
    
    }
    
    int square_side = 2 * guess;
    
    low = 0;
    high = 1000;
    
    while(1)
    {
        
        guess = (high + low) / 2;
        cout << "?" << " " << 0 << " " << guess << flush;
        cin >> i;
        
        if (abs(high - low) == 1)
            break;
        
        if (i == "YES")
            low = guess;
        else
            high = guess;
        
    }
    
    int ht_triangle = guess - square_side;
    
    low =0;
    high = 1000;
    
    while(1)
    {
        
        guess = (high + low) / 2;
        cout << "?" << " " << guess << " " <<  square_side << flush;
        cin >> i;
        
        if (abs(high - low) == 1)
            break;
        
        if (i == "YES")
            low = guess;
        else
            high = guess;
        
    }
    
    int base_triangle = 2 * guess;
    
    int area = (square_side * square_side) + (ht_triangle * base_triangle / 2);
    
    cout << "! " << area;
    

    
    
}
