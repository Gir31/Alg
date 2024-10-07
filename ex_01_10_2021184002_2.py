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
    for i in : # 두번째 녀석부터 끝까지 주인공 시키기
        pass
        #주인공 피신
        while ???: #어디까지 밀어주나
            pass #밀어주자
        #주인공이 들어갈 자리

def partition(arr, start, end):
    random_index = random.randint(start, end)
    # swap arr[start] and arr[random_index]

def quickSort(arr, start, end): # end = inclusive
    size = end - start + 1

    if size <= 5:
        # insertionSort(arr, start, end)
        return

    pivot_index = partition()
    quickSort(arr, start, pivot_index - 1)
    quickSort(arr, pivot_index + 1, end)


quickSort(words, 0, len(words) - 1)
insertionSort(words, 0, len(words) - 1)