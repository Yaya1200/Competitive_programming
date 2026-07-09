function isPowerOfThree(n: number): boolean {
    if(n < 1){
        return false
    }
    else if(n == 1){
        return true
    }
    return isPowerOfThree(n/3)
    
};