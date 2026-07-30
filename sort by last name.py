def sort_by_last_name(full_names):
    return sorted(full_names, key=lambda name: name.split()[-1])

if __name__ == "__main__":
    text = input("Enter full names separated by commas (e.g. John Smith, Amy Lee): ")
    names = [n.strip() for n in text.split(",") if n.strip()]
    print("Sorted by last name:", sort_by_last_name(names))