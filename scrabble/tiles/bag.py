from random import sample

fresh_bag = 'a' * 9 \
          + 'b' * 2 \
          + 'c' * 2 \
          + 'd' * 4 \
          + 'e' * 12 \
          + 'f' * 2 \
          + 'g' * 3 \
          + 'h' * 2 \
          + 'i' * 9 \
          + 'j' \
          + 'k' \
          + 'l' * 4 \
          + 'm' * 2 \
          + 'n' * 6 \
          + 'o' * 8 \
          + 'p' * 2 \
          + 'q' \
          + 'r' * 6 \
          + 's' * 4 \
          + 't' * 6 \
          + 'u' * 4 \
          + 'v' * 2 \
          + 'w' * 2 \
          + 'x' \
          + 'y' * 2 \
          + 'z' \
          + '*' * 2

def new_bag():
  return fresh_bag

def shake(bag):
  return ''.join(sample(bag, len(bag)))
