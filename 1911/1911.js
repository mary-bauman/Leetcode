/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAlternatingSum = function(nums) {
    let sumE = 0;
    let sumO = 0;
    for (let i = nums.length-1; i >= 0; i--){
        let tempE = Math.max(sumO + nums[i], sumE);
        let tempO = Math.max(sumE - nums[i], sumO);
        sumE = tempE;
        sumO = tempO;}
    return sumE;};
