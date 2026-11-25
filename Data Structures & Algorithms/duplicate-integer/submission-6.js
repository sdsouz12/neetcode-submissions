class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const visited =[]

        for(let number of nums)
        {
            if(visited.includes(number))
            {
                return true
            }
            visited.push(number)
        }
    
        return false
    }
}
