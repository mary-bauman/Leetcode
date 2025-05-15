function minOperations(grid: number[][], x: number): number {
    let result: number = 0;
    const a = grid.flat();
    a.sort((a, b) => a - b); //sort a as numbers instead of default str
    const n = a.length;
    const common: number = a[Math.floor(n/2)];
    const commonX: number = common%x;
    for (const num of a) {
        if (num%x != commonX) return -1
        result += Math.floor(Math.abs(common-num) / x)
    }
    return result;
};
