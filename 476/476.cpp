class Solution {
public:
    int findComplement(int num) {
        unsigned int mask = (1U << (32 - __builtin_clz(num))) - 1;
        return num ^ mask;
    }
};
