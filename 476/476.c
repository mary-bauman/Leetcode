int findComplement(int num) {
    int bits = 0;
    int n = num;

    while (n) {
        bits++;
        n >>= 1;
    }

    int mask = (1U << bits) - 1;
    return num ^ mask;
}
