# -- coding: utf-8 --


# Der Variable formatter wird ein String zugewiesen, der aus 4 raw datas besteht
formatter = "%r %r %r %r"

# formatter wird ausgegeben
# dabei werden die 4 raw datas ausgegeben,
# die in diesem Fall aus den Ziffern 1 bis 4 bestehen
print formatter % (1, 2, 3, 4)

# hier bestehen die vier raw datas aus den vier Strings "one" bis "four"
print formatter % ("one", "two", "three", "four")

# und hier bestehen die raw datas aus den boolean werten True und False
print formatter % (True, False, False, True)

# hier wird die variable formater selbst in die raw datas gepackt
# dadurch viermal der String '%r %r %r %r' ausgegeben
print formatter % (formatter, formatter, formatter, formatter)

# raw datas werden mit vier etwas längeren Strings gefüllt
# wegen des Kommas werden sie in einer Zeile durch ein Leerzeichen getrennt ausgegeben
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it din't sing.",
	"So I said goodnight."
)