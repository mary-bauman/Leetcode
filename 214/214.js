/**
 * @param {string} s
 * @return {string}
 */
var shortestPalindrome = function(s) {
    var n = s.length;
    var rs = s.split('').reverse().join('');
    for (let i = 0; i < n; i++){
        if (s.substring(0,n-i) == rs.substring(i,n)){
            return rs.substring(0,i) + s;
        }
    }
    return "";
};
