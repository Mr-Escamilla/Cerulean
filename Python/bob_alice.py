n = int(input("n = : "))
solutions = 0
for a in range(n + 1):
  for b in range(n + 1):
    c = n - (a + b)
    if c >= 0:
      # print(f"a:{a}, b:{b}, c:{c}")
      solutions += 1
  
print(f"solutions: {solutions}")