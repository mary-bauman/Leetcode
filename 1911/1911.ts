function maxAlternatingSum(nums: number[]): number {
    let sumE: number = 0;
    let sumO: number = 0;
    for (let i: number = nums.length-1; i >= 0; i--){
        let tempE: number = Math.max(sumO + nums[i], sumE);
        let tempO: number = Math.max(sumE - nums[i], sumO);
        sumE = tempE;
        sumO = tempO;}
    return sumE;};
