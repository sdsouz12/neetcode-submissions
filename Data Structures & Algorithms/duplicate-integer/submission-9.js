class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const visited = new Set()

        for(let num of nums){
            if(visited.has(num))
            {
                return true;
            }
            
            visited.add(num);
            
            }
            return false
        };


    
}
