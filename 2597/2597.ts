function beautifulSubsets(nums: number[], k: number): number {
    function dfs(nums: number[], k: number, i: number, s: Set<number>){
        if (i == nums.length){
            if (s.size === 0){return 0;}
            return 1;
        }
        let count = dfs(nums, k, i+1, s);
        if (s.has(nums[i]-k)){return count;}
        let newS: Set<number>  = new Set(s);
        newS.add(nums[i])
        return count + dfs(nums,k,i+1,newS);
    }

    nums.sort((a, b) => a - b);
    return dfs(nums,k, 0, new Set<number>());
};
