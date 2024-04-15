long long maxAlternatingSum(int* nums, int numsSize){
        long long sumEven = 0;
        long long sumOdd = 0;
        for (int i = numsSize-1; i >= 0; i--) {
            long long tempEven = fmax(sumOdd + nums[i], sumEven);
            long long tempOdd = fmax(sumEven - nums[i], sumOdd);
            sumEven = tempEven;
            sumOdd = tempOdd;
        }
        return sumEven;
}
