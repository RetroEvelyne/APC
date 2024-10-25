todo_list = [ "meet friends", "read book", "buy groceries" ]

print(todo_list)

todo_list[todo_list.index("meet friends")] = "meet fred"

print(todo_list)

todo_list.append("call mum")

print(todo_list)

todo_list += [ "clean room", "cook dinner" ]

print(todo_list)
