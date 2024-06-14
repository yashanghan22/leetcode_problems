import 'dart:math';

double rdCalculater(int years, double emi, double rate) {
  int months = (years * 12).toInt();
  double maturityAmount = 0.0;
  for (int i = months; i > 0; i--) {
    // print('-$i');
    var a = (emi * pow(1 + ((rate / 100) / 4), (4 * (i / months))));
    maturityAmount += a;
    // print('$i-=>${a.toStringAsFixed(2)}');
  }
  return maturityAmount;
}

void main() {
  print(rdCalculater(1, 500000, 6.5));
}
