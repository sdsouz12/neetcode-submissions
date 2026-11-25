class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let visited = {};

        for(let index =0; index< nums.length;index++){
            let difference = target - nums[index];

            if(difference in visited){
                return [visited[difference], index]
         }
            
            visited[nums[index]] = index


        }


    }
}
