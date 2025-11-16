def isHTML(html_file):


    stack = []
    split_html = html_file.split("<")
    i = 1

    while i < len(split_html):
        current_split = split_html[i]
        j = current_split.find('>')
        if j == -1:
            print("❌ Invalid: missing '>' in tag")
            return False
        word = current_split[:j]

        if word.startswith("/"):
            end_word = word[1:]
            if stack[-1] != end_word:
                print("❌ Invalid")
                return False
            stack.pop()
        else:
            stack.append(word)

        i += 1


    if len(stack) == 0:
        print("✅ HTML is valid")
        return True

    else:
        print("❌ Invalid")
        return False


tests = [
    "<html><body><p>Hello</p></body></html>",  # ✅ HTML valid
    "<div><span></span></div>",                # ✅ HTML valid
    "<div><span></div></span>",                # ❌ Invalid
    "<a><b></b></a>",                          # ✅ HTML valid
    "<a><b></a></b>",                          # ❌ Invalid
    "<div><p></p>",                            # ❌ Invalid
]

for t in tests:
    print(f"{t} -> {isHTML(t)}")



# basic_field = [
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0]
# ]
#
# def make_line(line: int, field) -> list:
#     new_line = []
#     for square_ind in range(len(field[line])):
#         if square_ind == 0:
#             if field[line-1][square_ind+1] == 1 and field[line-1][square_ind] == 0:
#                 new_line.append(1)
#             else:
#                 new_line.append(0)
#         elif square_ind == 9:
#             if field[line-1][square_ind-1] == 1 and field[line-1][square_ind] == 0:
#                 new_line.append(1)
#             else:
#                 new_line.append(0)
#         else:
#             if field[line-1][square_ind+1] == 1 and field[line-1][square_ind] == 0 and field[line-1][square_ind-1] == 0:
#                 new_line.append(1)
#             elif field[line-1][square_ind+1] == 0 and field[line-1][square_ind] == 0 and field[line-1][square_ind-1] == 1:
#                 new_line.append(1)
#             else:
#                 new_line.append(0)
#     return new_line
#
# def make_start(num: int) -> list:
#     new_field = basic_field.copy()
#     bin_num = bin(num)[2:]
#     for ind in range(-1, -len(bin_num) - 1, -1):
#         if bin_num[ind] == '1':
#             new_field[0][ind] = 1
#         elif bin_num[ind] == '0':
#             new_field[0][ind] = 0
#     return new_field
#
# def print_matrix(matrix):
#     for line in matrix:
#         print(*line)
#     print()
#
# for n in range(1, 1024):
#     game_field = make_start(n)
#     for i in range(1, 4):
#         game_field[i] = make_line(i, game_field)
#     if game_field[3] == [0,1,0,0,0,0,1,0,1,0]:
#         print_matrix(game_field)