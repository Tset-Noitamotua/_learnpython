# -*- coding: utf-8 -*-				| Schreibt man in die erste Zeile,
									| um die Kodierung des Queltextet festzulegen
									
=									| Zuweisungs-Zeichen
									| Damit lassen sich Werte, die sich auf der rechten
									| Seite von = ergeben, einer Variable auf der linken
									| Seite zuweisen
									
+, -, *, /							| Rechen-Operatoren
									| Addieren, Subtrahieren, Multiplizieren, Dividieren
									
print								| String oder Wert in der Konsole ausgeben

%s, %i, %d, %f						| Platzhalter, um Werte von Varialblen in
									| Strings einzubetten
									| %s --> String Variable
									| %i --> Integer Variable
									| %d --> double Variable
									| %f --> Float Variable
									
%.3f								| gibt Float Variable auf 3 Stellen hinter dem
									| Komma genau aus
									| z.B. 2.123
									
%.3s								| gibt seltsamerweise nur eine Stelle hinter dem
									| Komma aus. Benutzt man dagegen %s, werden so viel
									| Nachkommastellen angezeigt wie der Originalwert hatte
									
from sys import argv				| Importiert ein Feature aus einem bestimmten Modul
									| Hier aus dem Modul sys das Feature argv
									| Das importierte Feature kann direkt d.h.
									| ohne Pfadangabe verwendet werden
									| z.B. script, input_file = argv
									
import sys *						| Importiert ALLE Features des Moduls sys

argv								| ?

script, file1, file2 = argv			| ?

input()								|
raw_input()							|
open('file.txt')					|
xxx.read()							|
xxx.write()							|
xxx.seek(0)							| Spring an den Anfang einer (Text-)Datei
xxx.truncate()						|

\n, \t, \', \"						| Escaping Sequenzen (s. exercise ???)

#									| Kommentar Zeichen
"abc ... 123"						| String
'abc ... 123'						| String
"Ich hab's satt!"					| Einfaches Anführungszeichen im String
'Ich sagte: "Fick Dich!"'			| Doppelte Anführungszeichen im String

len(xxx)							| Gibt die Größen von xxx in bytes an.
									| Ist xxx ein String, dann entspricht das der
									| Anzahl der Zeichen im String
									

























