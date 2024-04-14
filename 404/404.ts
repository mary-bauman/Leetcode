/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumOfLeftLeaves(root: TreeNode | null): number {
    let queue = [root];
    let left = 0;
    while (queue.length>0){
        for (let i = 0; i < queue.length; i++){
            let node = queue.shift();
            if (node.left){
                if ((!node.left.left) && (!node.left.right)){
                    left += node.left.val
                }
                queue.push(node.left);
            }
            if (node.right){
                queue.push(node.right)}}}
    return left;};
