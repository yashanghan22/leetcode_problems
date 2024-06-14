import 'dart:math';

int maxDepth(TreeNode? root) {
  if (root == null) {
    return 0;
  }
  int left = maxDepth(root.left);
  int right = maxDepth(root.right);
  print('${max(left, right) + 1}');
  return max(left, right) + 1;
}

void main() {
  maxDepth(TreeNode(3));
  maxDepth(TreeNode(
      3, TreeNode(9, TreeNode(2)), TreeNode(20, TreeNode(15), TreeNode(7))));
}

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}
