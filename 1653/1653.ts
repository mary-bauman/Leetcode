function minimumDeletions(s: string): number {
    let bs: number = 0;
    let count: number = 0;
    for (var i: number = 0; i < s.length; i++){
        if (s.charAt(i)=='a') count = Math.min(count+1, bs);
        else bs+=1;
    }

    return count;
};
