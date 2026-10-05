def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


if __name__ == "__main__":
    lst = [1, 2, 3, 2, 4, 5, 3]
    result = find_duplicates(lst)
    print(result)