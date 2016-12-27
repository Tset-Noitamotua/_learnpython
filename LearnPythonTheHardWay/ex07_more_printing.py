# -- coding: utf-8 --

# String ausgeben
print "Mary had a little lamb."

# String ausgeben, wobei an der Stelle von %s der String 'snow' eingefügt wird
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."

# Der String . (Punkt) wird 10mal ausgegeben
print "." * 10 # kkommentar

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# Strings end1 bis end6 werden mit einander verbunden und ausgegeben
# Das Komma am Ende sorgt dafür, dass die nächste print Ausgabe in der gleichen Zeile
# mit einem Leerzeichen voran fortgesetzt wird (ansonsten würde die Ausgabe in der
# nächsten Zeile erfolgen)
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
