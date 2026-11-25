/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {

        const result =[]

        const q = [root]

        while(q.length >0){
            let qLen = q.length
            let lvl =[]
            for( let i = 0 ; i < qLen; i++ ){
                let node = q.shift()

                if(node){
                    lvl.push(node.val);
                    q.push(node.left);
                    q.push(node.right);
                }


            }
            if(lvl.length >0){
                result.push(lvl)
            }
   
        }
 return result

    }
}
