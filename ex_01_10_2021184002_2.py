import random

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

    for i in range(left + 1, right + 1, 1):
        for j in range(i, left, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

def partition(arr, start, end):
    random_index = random.randint(start, end)

    l, r = start, end

    pivot = arr[random_index]

    while True:
        while pivot < arr[l]: l += 1 # 피봇에서 왼쪽 값중 피봇보다 작은 값 찾기
        while pivot > arr[r]: r -= 1 # 피봇에서 오른쪽 값중 피봇보다 큰 값 찾기

        arr[l], arr[r] = arr[r], arr[l] # 찾으면 바꾸기

        if l >= r: break
        
    return l

def quickSort(arr, start, end): # end = inclusive
    size = end - start + 1

    if size <= 5:
        # insertionSort(arr, start, end)
        return

    pivot_index = partition(arr, start, end)
    quickSort(arr, start, pivot_index - 1)
    quickSort(arr, pivot_index + 1, end)


if __name__ == '__main__':
    quickSort(words, 0, len(words) - 1)
    insertionSort(words, 0, len(words) - 1)

    print('--- Quick Sort ---')
    print(words)