int calcGCD(int n, int m){
    if (m>n){

        int temp = m;
        m = n;
        n = temp;
    }

    while(n%m != 0){
        int rem = n%m;
        n = m;
        m = rem;
    }
    
    return m;
}
