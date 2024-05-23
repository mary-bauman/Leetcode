function beautifulSubsets(nums: number[], k: number): number {
    function dfs(nums: number[], k: number, i: number, s: Set<number>){
        if (i == nums.length){return s.size === 0 ? 0 : 1;}
        let count = dfs(nums, k, i+1, s);
        if (s.has(nums[i]-k)){return count;}
        return count + dfs(nums,k,i+1,new Set([...s, nums[i]]));
    }
    return dfs(nums.sort((a, b) => a - b), k, 0, new Set<number>());
};
