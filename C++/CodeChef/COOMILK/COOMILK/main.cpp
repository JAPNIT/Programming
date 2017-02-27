//
//  main.cpp
//  COOMILK
//  https://www.codechef.com/LTIME45/problems/COOMILK
//  Created by Japnit Kaur Ahuja on 27/02/17.
//  Copyright © 2017 Japnit Kaur Ahuja. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int t0=0; t0<t; t0++)
    {
        int n;
        cin >> n;
        string w;
        
        vector <string> word;
        
        for(int n0=0; n0<n; n0++)
        {
            cin >> w;
            word.push_back(w);
            
        }
        
        for(int n0=0; n0<n; n0++)
        {
            if ((n==1 && word[0] == "cookie") || (word[n0] == "cookie" && word[n0+1] == "cookie") )
            {
                w="NO";
                break;
            }
            
            else
                w="YES";
            
        }
        
        cout << w;
    }

}
