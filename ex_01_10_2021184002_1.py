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

def insertionSort(arr, left, right): #right = inclusive
    pass

def mergeSort(arr, start, end): # end = inclusive
 
    size = end - start + 1

    if size <= 5: 
        insertionSort(arr, start, end)
        return

    first_right = (start + end) // 2 + 1

    mergeSort(arr, start, first_right - 1)
    mergeSort(arr, first_right, end)
    merge(arr, start, first_right, end)

def merge(arr, start, mid, end): # mid = first right

    merged = []

    l, r = start, mid

    while l < mid and r <= end:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:  
            merged.append(arr[r])
            r += 1

    while l < mid:
        merged.append(arr[l])
        l += 1
    
    while r <= end:
        merged.append(arr[r])
        r += 1

    l = start

    for i in merged:
        arr[l] = i
        l += 1

    pass

mergeSort(words, 0, len(words) - 1)
print(words)