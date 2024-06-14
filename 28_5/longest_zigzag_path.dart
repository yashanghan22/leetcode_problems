import 'max_depth_binary_tree.dart';

int count = 0;
bool isLeft = true;
int longestZigZag(TreeNode? root) {
  if (root == null) return 0;
  print('${root.val}');
  // if (root.left != null || root.right != null) {
  count++;
  // }
  longestZigZag(isLeft && root.left != null ? root.left : root.right);
  // longestZigZag(root.right);
  if (root.left == null) {
    isLeft = false;
  } else {
    isLeft = !isLeft;
  }
  // if (root.left != null) {
  //   count++;
  //   isLeft=false;
  //   longestZigZag(root.left);
  // }
  // if (root.right != null) {
  //   count++;
  //   isLeft=true;
  //   longestZigZag(root.right);
  // }
  return count;
}

void main() {
  // var root = TreeNode(
  //   1,
  //   TreeNode(2, null, TreeNode(3, TreeNode(4, null, TreeNode(5)), TreeNode(6))),
  //   TreeNode(7),
  // );
  var root = TreeNode(
      1,
      null,
      TreeNode(
          1,
          TreeNode(1),
          TreeNode(1, TreeNode(1, null, TreeNode(1, null, TreeNode(1))),
              TreeNode(1))));
  print("-=>" + longestZigZag(root).toString());
}
