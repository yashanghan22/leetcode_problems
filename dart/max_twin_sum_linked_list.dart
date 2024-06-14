import 'delete_middle_node.dart';

int pairSum(ListNode? head) {
  List<int> oddList = [];
  List<int> evenList = [];
  while (head != null) {
    if (head.val.isEven) {
      evenList.add(head.val);
    } else {
      oddList.add(head.val);
    }
    head = head.next;
  }
  if (oddList.length + evenList.length < 3) {
    var list = (oddList + evenList).toList();
    return list.reduce((value, element) => value + element);
  }
  var odd = oddList.reduce((value, element) => value + element);
  var even = evenList.reduce((value, element) => value + element);
  // for (var i = 0; i < mainList.length; i++) {
  //   for (var j = 0; j < mainList.length; j++) {
  //     if (i != j) {
  //       if (max < (mainList[i] + mainList[j])) {
  //         max = mainList[i] + mainList[j];
  //       }
  //     }
  //   }
  // }
  return odd > even ? odd : even;
}

void main() {
  print(
      pairSum(ListNode(1, ListNode(2, ListNode(0, ListNode(4, ListNode(5)))))));
}
