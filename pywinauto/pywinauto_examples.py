from pywinauto import application

app = application.Application(backend='uia')
app.start("notepad.exe")

app['Unbenannt - Editor'].wait('visible')
app['Unbenannt - Editor'].set_focus()
app['Unbenannt - Editor'].draw_outline()
app['Unbenannt - Editor'].print_control_identifiers()
app['Unbenannt - Editor'].menu_select("Bearbeiten -> Ersetzen")
app['Unbenannt - Editor'].print_control_identifiers()
app['Unbenannt - Editor'].ErsetzenDialog.draw_outline()

app['Unbenannt - Editor'].ErsetzenDialog.print_control_identifiers()
app['Unbenannt - Editor'].ErsetzenDialog.Abbrechen.click()

app['Unbenannt - Editor'].Edit.draw_outline()
app['Unbenannt - Editor'].Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
app['Unbenannt - Editor'].menu_select("Datei -> Beenden")
app['Unbenannt - Editor'].print_control_identifiers()
app['Unbenannt - Editor'].EditorDialog.Nicht_speichern.click()










# from pywinauto import Desktop, Application
# app = Application(backend='uia').start('notepad.exe')

# #np_editor = app.window(title='Unbenannt - Editor')
# np_editor = app['Unbenannt - Editor']

# np_editor.set_focus()
# np_editor.draw_outline('red')
# np_editor.print_control_identifiers()
# np_editor.TitelBar.draw_outline('red')
# np_editor.Minimieren.draw_outline('blue')
# np_editor.Schließen.draw_outline('green')
# np_editor.Maximieren.draw_outline('yellow')

# np_editor.maximize()
# np_editor.minimize()
# app.kill()



##################################################################################
# Application().start('explorer.exe "C:\Program Files"')

# # connect to another process spawned by explorer.exe
# app = Application(backend="uia").connect(path="explorer.exe", title="Programme")

# app.Programme.set_focus()
# app.Programme.draw_outline('read')
# app.Programme.ListBox.draw_outline('green')

# common_files = app.Programme.ListBox.get_item('Common Files')
# common_files.draw_outline('blue')
# common_files.right_click_input((50,5))
# app.ContextMenu['Eigenschaften'].invoke()


# # this dialog is open in another process (Desktop object doesn't rely on any process id)
# Properties = Desktop(backend='uia').Eigenschaften_von_Common_Files
# Properties.print_control_identifiers()
# Properties['Abbrechen'].click()
# Properties.wait_not('visible') # make sure the dialog is closed

