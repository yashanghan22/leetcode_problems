String predictPartyVictory(String senate) {
  List<String> r = [];
  List<String> d = [];
  for (var i = 0; i < senate.length; i++) {
    if (senate[i].toLowerCase() == 'r') {
      r.add(senate[i]);
    }
    if (senate[i].toLowerCase() == 'd') {
      d.add(senate[i]);
    }
  }
  var diff = r.length - d.length;

  return diff > 0 ? 'Radiant' : 'Dire';
}

void main() {
  print(predictPartyVictory('RDRDRRRRRRRDRDRDRD'));
}
