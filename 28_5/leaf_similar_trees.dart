import 'max_depth_binary_tree.dart';

bool leafSimilar(TreeNode? root1, TreeNode? root2) {
  List<int> array1 = res(root1, []);
  List<int> array2 = res(root2, []);
  // array1.sort();
  // array2.sort();
  // print('arr1:$array1//arr2:$array2');
  return array1.join(',') == array2.join(',');
}

List<int> res(TreeNode? root, List<int> arr) {
  if (root == null) {
    return [];
  }
  if (root.left == null && root.right == null) {
    arr.add(root.val);
  }
  res(root.left, arr);
  res(root.right, arr);
  return arr;
}

void main() {
  var root1 = TreeNode(1, TreeNode(3), TreeNode(2));
  var root2 = TreeNode(1, TreeNode(2), TreeNode(3));
  // var root1 = TreeNode(
  //     3,
  //     TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
  //     TreeNode(1, TreeNode(9), TreeNode(8)));
  // var root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)),
  //     TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))));
  print('-=>${leafSimilar(root2, root1)}');
}
