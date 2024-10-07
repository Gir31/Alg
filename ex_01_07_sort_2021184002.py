array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268, 
]

count = len(array)

def sort_bubble(arr):
  print('=' * 60)
  print(f'before: {arr}')
  for a in range(count - 1):
    for b in range(count - a - 1):
      if arr[b] > arr[b + 1] :
        arr[b], arr[b+1] = arr[b+1], arr[b]
  print(f'after : {arr}')

def sort_select(arr):
  print('=' * 60)
  print(f'before: {arr}')
  for a in range(count - 1):
    min_at = a
    for b in range(a + 1, count):
      if arr[min_at] > arr[b]:
        min_at = b
    arr[a], arr[min_at] = arr[min_at], arr[a]
  print(f'after : {arr}')

def sort_insert(arr):
  print('=' * 60)
  print(f'before: {arr}')
  for a in range(1, count) :
    pivot = arr[a]
    b = a
    while b > 0:
      if arr[b - 1] > pivot:
        arr[b] = arr[b - 1]
        b -= 1
      else: 
        break
    arr[b] = pivot

  print(f'after : {arr}')

def sort_shell(arr):
  print('=' * 60)
  print(f'before: {arr}')
  for gap in [31, 15, 7, 3, 1, 0]:
    for a in range(gap):
      for b in range(gap+a, count, gap):
        pivot = arr[b]
        c = b
        while c > 0:
          if arr[c - gap] > pivot:
            arr[c] = arr[c - gap]
            c -= gap
          else:
            break
        arr[c] = pivot

  print(f'after : {arr}')

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])

if __name__ == '__main__':
  main()

