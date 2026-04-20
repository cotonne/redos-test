import re

def test_pattern(s: str):
  p = re.compile("\\[.*\\]")
  return p.match(s)

if __name__ == "__main__":
  test_str = "[ok]"
  if test_pattern(test_str):
    print("OK")
  else:
    print("KO")
