String decodeString(String s) {
  String currentStr = '';
  int currentNum = 0;
  List<String> stack = [];

  for (int i = 0; i < s.length; i++) {
    String char = s[i];

    if (isDigit(char)) {
      currentNum = currentNum * 10 + int.parse(char);
      print('$i-$currentNum-${char}');
    } else if (char == '[') {
      stack.add(currentStr);
      stack.add(currentNum.toString());
      currentStr = '';
      currentNum = 0;
    } else if (char == ']') {
      int num = int.parse(stack.removeLast());
      String prevStr = stack.removeLast();
      currentStr = prevStr + currentStr * num;
    } else {
      currentStr += char;
    }
    print('->$currentStr -$stack');
  }

  return currentStr;
}

bool isDigit(String char) {
  return RegExp(r'\d').hasMatch(char);
}

void main() {
  String encodedString = "3[a]2[bc]";
  // String encodedString = "3[a18[b]2[c]]";
  // String encodedString = "2[abc]3[cd]ef";
  print(decodeString(encodedString)); // Output should be "aaabcbc"
}
