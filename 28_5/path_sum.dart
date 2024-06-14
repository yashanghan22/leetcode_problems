import 'max_depth_binary_tree.dart';

int sum = 0;
int pathSum(TreeNode? root, int targetSum) {
  // List<int?> list = [];
  if (root == null) return 0;
  // list.add(root.val);
  // if (root.left != null || root.right != null) {
  //   list.add(root.left?.val);
  //   list.add(root.right?.val);
  // }
  // // while(root!=null){
  // //   // root
  // //   // if(root.va)
  // // }
  // print('$list');
  dfs(root, targetSum);
  pathSum(root.left, targetSum);
  pathSum(root.right, targetSum);
  return sum;
}

dfs(TreeNode? node, int currSum) {
  if (node == null) return;
  if (node.val == currSum) sum++;
  print('$currSum-${node.val}=${currSum - node.val}');
  dfs(node.left, currSum - node.val);
  dfs(node.right, currSum - node.val);
}

void main() {
  var root = TreeNode(
      10,
      TreeNode(
        5,
        TreeNode(3, TreeNode(3), TreeNode(-2)),
        TreeNode(2, null, TreeNode(1)),
      ),
      TreeNode(-3, null, TreeNode(11)));
  print(pathSum(root, 8));
}
