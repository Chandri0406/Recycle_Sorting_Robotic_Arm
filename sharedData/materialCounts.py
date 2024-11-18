materialCounts = {
    "cardboard": 0,
    "glass": 0,
    "metal": 0,
    "paper": 0,
    "plastic": 0,
}

def updateCounts(counts, label):
    counts[label] += 1

def sortedMaterials():
    return materialCounts