//Moores algo which is the optimal solution
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidate = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }

        
        int cnt1 = 0;
        for (int num : nums) {
            if (num == candidate) cnt1++;
        }
        if (cnt1 > nums.size() / 2) return candidate;
        return -1;

        
    }
};
