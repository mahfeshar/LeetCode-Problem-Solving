class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) return false;
        long long temp = x;
        long long reversed = 0;
        for(int i = 0; temp != 0; i++){
            reversed = reversed * 10 + temp % 10;
            temp /= 10;
        }
        return (reversed == x);
    }
};