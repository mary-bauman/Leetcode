function shortestPalindrome(s: string): string {
    var n: number = s.length;
    var rs: string = s.split('').reverse().join('');
    for (let i: number = 0; i < n; i++){
        if (s.substring(0,n-i) == rs.substring(i,n)){
            return rs.substring(0,i) + s;
        }
    }
    return "";
};
