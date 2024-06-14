import 'delete_middle_node.dart';

ListNode? reverseList(ListNode? head) {
  List<int> mainList = [];
  while (head != null) {
    mainList.add(head.val);
    head = head.next;
  }
  mainList = mainList.reversed.toList();
  print('$mainList');
  if (mainList.isNotEmpty) {
    ListNode res = ListNode(mainList[0]);
    ListNode tem = res;
    for (var i = 1; i < mainList.length; i++) {
      var node = ListNode(mainList[i]);
      tem.next = node;
      tem = node;
    }
    print('${res.toString()}');
    return res;
  }
  return null;
}

void main() {
  reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))));
}
