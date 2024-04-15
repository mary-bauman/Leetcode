class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        long long sumOdd = 0;
        long long sumEven = 0;

        for(auto it = nums.rbegin(); it != nums.rend(); ++it) {
            long long tempEven = max(sumOdd + *it, sumEven);
            long long tempOdd = max(sumEven - *it, sumOdd);
            sumOdd = tempOdd;
            sumEven = tempEven;
        }

        return sumEven;
    }
};
