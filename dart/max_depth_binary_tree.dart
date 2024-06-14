int maxDepth(TreeNode? root) {
  List<int?> list = [];
  while (root != null && (root.left != null || root.right != null)) {
    list.add(root.val);
    list.add(root.left?.val);
    list.add(root.right?.val);
    if (root.left?.left == null || root.left?.right == null) {
      list.add(root.left?.left?.val);
      list.add(root.left?.right?.val);
    }
    // while (root?.left?.left != null || root?.left?.right != null) {
    //   list.add(root?.left?.left?.val);
    //   list.add(root?.left?.right?.val);
    //   root = root?.left?.left;
    // }
    // while (root?.right?.left != null || root?.right?.right != null) {
    //   list.add(root?.right?.left?.val);
    //   list.add(root?.right?.right?.val);
    //   root = root?.right?.right;
    // }
    // root.val=;
    root.left = root.left?.left;
    root.right = root.right?.right;
  }
  print(list);
  return 0;
}

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

void main() {
  maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))));
}
