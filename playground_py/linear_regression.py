def predict(alpha, betta, x):
  return betta * x + alpha

def error():
  return y - predict(alpha, betta, x)