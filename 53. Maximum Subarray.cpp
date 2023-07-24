class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum=INT_MIN;    
        int curr_sum=0;
        for(int j=0;j<nums.size();j++){
            curr_sum+=nums[j];
            if(curr_sum>max_sum){
                max_sum=curr_sum;
            }
            if(curr_sum<0){
                curr_sum=0;
            }
        }
        
        return max_sum;
        
    }
    
};
