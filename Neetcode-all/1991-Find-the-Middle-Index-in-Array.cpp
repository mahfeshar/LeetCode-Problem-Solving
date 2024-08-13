class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n + 1, 0);
        vector<int> post(n + 1, 0);
        for(int i = 0; i < n; i++)
        {
            if(i){
                pre[i] = pre[i-1] + nums[i];
            }
            else{
                pre[i] = nums[i];
            }
            post[n-i-1] = post[n-i] + nums[n-i-1];
        }
        if (post[1] == 0 || n == 1)
            return 0;
        for(int i = 1; i < n-1; i++){
            if (pre[i-1] == post[i+1]){
                return i;
            }
        }
        if (pre[n-2] == 0)
            return n-1;
        return -1;
    }
};