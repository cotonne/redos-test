import re

def test_pattern(s: str):
  patterns = [
    re.compile("\\[.*\\]"),
    re.compile("<\\s*img[^>]*>.*?<\\s*/\\s*img\\s*>"),
    re.compile("A(B|C+)+D"),
  ]
  return any(p.match(s) for p in patterns)

if __name__ == "__main__":
  test_str = "[ok]"
  if test_pattern(test_str):
    print("OK")
  else:
    print("KO")
