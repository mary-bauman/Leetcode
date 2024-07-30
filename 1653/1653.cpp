class Solution {
  public:
      int minimumDeletions(string s) {
          int bs = 0;
          int deletions = 0;
          for(char& c : s) {
              if (c=='a'){deletions = min(deletions+1, bs);}
              else{bs+=1;}
          }
          return deletions;
      }
};
