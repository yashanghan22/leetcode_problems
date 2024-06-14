import 'delete_middle_node.dart';

ListNode? oddEvenList(ListNode? head) {
  List<int> mainList = [];
  List<int> evenList = [];
  while (head != null) {
    if (head.val.isEven) {
      evenList.add(head.val);
    } else {
      mainList.add(head.val);
    }
    head = head.next;
  }
  print('$mainList-$evenList');
  mainList.addAll(evenList);
  if (mainList.isNotEmpty) {
    ListNode res = ListNode(mainList[0]);
    ListNode tem = res;
    for (var i = 1; i < mainList.length; i++) {
      var node = ListNode(mainList[i]);
      tem.next = node;
      tem = node;
    }
    // print('${res.toString()}');
    return res;
  }
  return null;
}

void main() {
  // print('');
  oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))));
}
