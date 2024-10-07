from time import time

words = [

  '2021184002', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'class01', 'idolize', 'romance', 'overestimate', 'revive', 'smell', 

  'toast', 'singe', 'inlay', 'field', 'speed', 'farad', 'adult', 'pansy', 'crawl', 'smith', 'exude', 

  'froze', 'litho', 'inuit', 'fakir', 'noddy', 'sheen', 'sandy', 'gaffe', 'spark', 'cavil', 'tenor', 

  'clonk', 'stung', 'boult', 'inapt', 'taker', 'cliff', 'shine', 'sable', 'agile', 'evens', 'pluck', 

  'blade', 'niece', 'paste', 'theft', 'young', 'bonny', 'aggro', 'bevel', 'rebel', 'clown', 'quote', 

  'horsy', 'wrong', 'hindu', 'acute', 'sloop', 'tuner', 'expel', 'motel', 'divan', 'gesso', 'strop', 

  'lance', 'lifer', 'dunce', 'lemur', 'scree', 'basic', 'wring', 'graph', 'conch', 'favor', 'anise', 

  'value', 'queue', 'poppy', 'staid', 'snook', 'spurt', 'canto', 'sprat', 'first', 'sidle', 'douse', 

]




def down_heap(root, size):
  lc = root * 2 + 1 
  if lc >= size: return 
  child = lc
  rc = root * 2 + 2  
  if rc < size: 
    if array[rc] > array[lc]: 
      child = rc        

  if array[root] < array[child]: 
    array[root], array[child] = array[child], array[root]
    down_heap(child, size)



def main():
  print('before:', array)
  count = len(array)

  last_parent_index = count // 2 - 1
  for n in range(last_parent_index, -1, -1):
    down_heap(n, count)

  last_sort_index = count - 1
  while last_sort_index > 0:
    array[0], array[last_sort_index] = array[last_sort_index], array[0] 
    down_heap(0, last_sort_index) 
    last_sort_index -= 1
  print('after :', array)

if __name__ == '__main__':
  while True:
    array = words
    startedOn = time()
    main()
    elapsed = time() - startedOn
    print(f'Elapsed time = {elapsed:.3f}s')
    break;
