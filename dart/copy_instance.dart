class Person {
  String name;
  Person({required this.name});
}

void main() {
  var p1 = Person(name: 'yash');
  var p2 = p1;
  p2.name = 'yes';
  print('${p1.name}');
}
