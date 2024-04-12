int trap(int* height, int heightSize) {
    int sm = 0;
    int pre[heightSize]; int suf[heightSize];
    for (int i = 0; i < heightSize; i++) pre[i] = 0;
    for (int i = 0; i < heightSize; i++) suf[i] = 0;
    pre[0] = height[0];

    for (int i = 1; i < heightSize; i++){
        pre[i] = pre[i-1];
        if (height[i]>pre[i-1]){
            pre[i] = height[i];}}

    suf[heightSize-1] = height[heightSize-1];

    for (int i = heightSize - 2; i >= 0; i--) {
        suf[i] = (height[i] > suf[i + 1]) ? height[i] : suf[i + 1];}
    
    for (int i = 0; i < heightSize; i++) {
        sm += (((suf[i] < pre[i]) ? suf[i] : pre[i]) - height[i]);}

    return sm;}
