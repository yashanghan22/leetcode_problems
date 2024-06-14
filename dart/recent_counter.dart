class RecentCounter {
  List<int> list = [];
  RecentCounter() {}

  int ping(int t) {
    if (list.length == 0) {
      list.add(t);
      return 1;
    } else {
      if (t <= 3000) {
        list.add(t);
      } else {
        int margin = t - 3000;
        while (list.isNotEmpty && list.first < margin) {
          list.removeAt(0);
        }
        list.add(t);
      }
      return list.length;
    }
  }
}

void main() {
  RecentCounter recentCounter = new RecentCounter();
  print(recentCounter.ping(1));
  print(recentCounter.ping(100));
  print(recentCounter.ping(3001));
  print(recentCounter.ping(3002));
}
