/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    var bs = 0;
    var count = 0;
    for (var i = 0; i < s.length; i++){
        if (s.charAt(i)=='a') count = Math.min(count+1, bs);
        else bs+=1;
    }

    return count;
};
