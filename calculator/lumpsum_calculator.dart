double lumpsumCalculater(int years, double amount, double rate) {
  int months = (years).toInt();
  double maturityAmount = amount;
  for (int i = months; i > 0; i--) {
    // print('-$i');
    maturityAmount += (maturityAmount * (rate / 100));
    // print('$i-=>${a.toStringAsFixed(2)}');
  }
  return maturityAmount;
}

void main() {
  print(lumpsumCalculater(2, 100000, 10));
}
