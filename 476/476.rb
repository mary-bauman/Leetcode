impl Solution {
    pub fn find_complement(num: i32) -> i32 {
        let bits = 32 - num.leading_zeros();
        let mask = (1u32 << bits) - 1;
        (num as u32 ^ mask) as i32
    }
}
