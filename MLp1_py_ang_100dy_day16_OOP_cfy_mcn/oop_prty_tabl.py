
import prettytable

table = prettytable.PrettyTable()

# Adding columns
table.add_column("Bilie", ["Cry", "Work", "Crap", "Drink", "work", "cry"])
table.add_column("Meesy", ["Laugh", "Work", "Shit", "Play", "Work", "Laugh"])

# align: Justify text to left
# Use "align" attribute. The allowed strings are "l", "r" and "c" for left, right and centre alignment, respectively
table.align = "l"

print(table)


# python oop_prty_tabl.py