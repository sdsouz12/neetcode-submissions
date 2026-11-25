class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
          if(s.length !== t.length){
            return false
          }

          const countS = this.getCount(s);
          const countT = this.getCount(t) ; 

          for (let char in countS){
            if(countS[char] !== countT[char]){
                return false
            }
          }  

        return true
    
    }

    getCount(s) {
        let count ={}
        for( let char of s){
            if(count.hasOwnProperty(char)){
                count[char]++;
            }
            else{
                count[char] = 1;
            }

            
        }
        return count;
    }
}
