import 'dart:developer';

class Solution {
  ListNode? deleteMiddle(ListNode? head) {
    List<int> list = [];
    var curr = head;
    var nxt = head?.next;
    while (curr != null) {
      list.add(curr.val);
      curr = nxt;
      nxt = nxt?.next;
    }
    if (list.isNotEmpty) {
      list.removeAt(list.length ~/ 2);
    }
    if (list.isEmpty) return null;
    ListNode res = ListNode(list[0]);
    ListNode temp = res;
    for (var i = 1; i < list.length; i++) {
      var node = ListNode(list[i]);
      temp.next = node;
      print('0->${temp.val}');
      temp = node;
      print('1->${temp.val}');
      print('res->${res.toString()}');
      // res.next = ListNode(list[i]);
      // res = res.next ?? ListNode();
    }
    // print('-=>${res.toString()}');
    return null;
  }
}

void main() {
  Solution().deleteMiddle(
      ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))));
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);

  @override
  String toString() {
    ListNode? node = this.next;
    print('$val');
    while (node != null) {
      print('${node.val}');
      node = node.next;
    }
    return super.toString();
  }
}
