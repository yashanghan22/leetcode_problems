bool canPlaceFlowers(List<int> flowerbed, int n) {
  int count = n.toInt();
  if (n == 0) return true;
  for (var i = 0; i < flowerbed.length; i++) {
    if (flowerbed[i] == 0 &&
        (i == 0 || flowerbed[i - 1] == 0) &&
        (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
      print('$i');
      flowerbed[i] = 1;
      count--;
    }
    if (count == 0) {
      return true;
    }
  }
  print('$count $flowerbed');
  return false;
}

void main() {
  print(canPlaceFlowers([0, 0, 0, 0, 0, 1], 2));
}
