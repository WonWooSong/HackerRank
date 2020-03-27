def checkMagazine(magazine, note):
    magazineCounter = Counter(magazine)
    noteCounter = Counter(note)
    if noteCounter - magazineCounter == {}:
        print("Yes")
    else:
        print("No")
