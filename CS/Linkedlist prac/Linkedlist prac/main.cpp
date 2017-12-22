#include <iostream>
using namespace std;


int minimum(int n,int k)
{
    int ctr=0;
    while(n>0)
    {
        ctr++;
        n=n-k;
        
    }
    
    return ctr;
        
    
    
}

void ways(int n)
{
    cout << n;
    if(n>0)
        ways(n-1);
    
    
}



int main()
{
    int n,k,min;
    cin >> n >> k;
    
    min = minimum(n,k);
    
    cout << "min " << min << endl;
    
    ways(9);
    return 0;
}
