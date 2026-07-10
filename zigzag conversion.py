def convert_zigzag(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s
    rows = [""] * num_rows
    curr_row = 0
    going_down = False
    for char in s:
        rows[curr_row] += char
        if curr_row == 0 or curr_row == num_rows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1
   return ''.join(rows)
if __name__ == "__main__":
    text = input("Enter a string: ").strip()
    try:
        rows = int(input("Enter number of rows: "))
        print(convert_zigzag(text, rows))
    except ValueError:
        print("Please enter a valid number for rows.")
