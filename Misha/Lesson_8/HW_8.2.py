month = int(input("Enter a month: "))
match month:
    case 1 | 3 | 5 | 7 | 9 | 11:
        print("31")
    case 4 | 6 | 8 | 10 | 12:
        print("30")
    case 2:
        print("28")
    case _:
        print("Invalid month")