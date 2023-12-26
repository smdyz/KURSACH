import funcs

for element in funcs.latest_opers():
    if "from" in element.keys():
        funcs.print_oper(element["date"], element["description"], element["to"],
                         element["operationAmount"]["amount"], element["operationAmount"]["currency"]["name"],
                         element["from"])
        print("\n\n\n")
    else:
        funcs.print_oper(element["date"], element["description"], element["to"],
                         element["operationAmount"]["amount"], element["operationAmount"]["currency"]["name"])
        print("\n\n\n")

