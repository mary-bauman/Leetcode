function trap(height: number[]): number {
    let sm: number = 0
    let n: number = height.length
    const pre: number[] = Array(n).fill(0)
    const suf: number[] = Array(n).fill(0)

    pre[0] = height[0]

    for (let i: number = 1; i < n; i++){
        pre[i] = Math.max(pre[i-1], height[i])}

    suf[n-1] = height[n-1]

    for (let i = n-2; i>=0;i--){
        suf[i] = Math.max(suf[i+1], height[i])}
    
    for (let i = 0; i < n; i++){
        sm += Math.min(suf[i],pre[i]) - height[i]}

    return sm};
