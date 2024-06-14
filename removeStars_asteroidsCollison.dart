String removeStars(String s) {
  List<String> list = [];
  int r = 0;
  while (r < s.length) {
    if (s[r] == '*') {
      list.removeLast();
    }
    if (s[r] != '*') {
      list.add(s[r]);
    }
    r++;
  }
  print('$list');
  return list.join();
}

List<int> asteroidCollision(List<int> asteroids) {
  List<int> list = [];
  int r = 1;
  int l = 0;
  while (r <= (asteroids.length - 1)) {
    if ((asteroids[r] > 0 && asteroids[l] > 0) ||
        (asteroids[r] < 0 && asteroids[l] < 0)) {
      print('1-=>$r $l - ${asteroids[r]} ${asteroids[l]}');
      list.add(asteroids[l]);
      // list.add(asteroids[r]);
    }
    if (asteroids[r] > 0 && (asteroids[l] < 0)) {
      print('2-=>$r $l - ${asteroids[r]} ${asteroids[l]}');
      int a = (asteroids[r] > (-asteroids[l])) ? asteroids[r] : asteroids[l];
      list.add(a);
    }
    if (asteroids[r] < 0 && (asteroids[l] > 0)) {
      print('3-=>$r $l - ${asteroids[r]} ${asteroids[l]}');
      int a = ((-asteroids[r]) > asteroids[l]) ? asteroids[r] : (asteroids[l]);
      list.add(a);
    }
    r++;
    l++;
  }
  if (list.any((element) => element.isNegative)) {
    return asteroidCollision(list);
  }
  print('$list');
  return list;
}

void main() {
  asteroidCollision([8 - 8]);
}
