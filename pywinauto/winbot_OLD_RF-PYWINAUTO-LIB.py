###
# pyWinAuto library for Robot Framework
###

# TODO: Need to do verification that each of the controls passed in are actually that control type. This is for each type of control command.
# TODO: Don't have anything handling tooltips in here. Kinda need to do that.

from pywinauto import application as pwa
import pywinauto

class winbot:
    __version__ = '0.3'
    
    def __init__(self):
        self.app = None
        self.dlg = None
    
    def winSetTimeout(self, timeout_type, new_timeout_time):
        """
        Set the timeout value to something other than the defaults. Below are the acceptable timeout types, and thier associated timeout defaults.
        
        Also acceptable are the timeout type of "default" and the timeout time of "fast", "slow" or "default". These are predefined timeout templates.
        
        * window_find_timeout (default 3)
        * window_find_retry (default .09)
        * app_start_timeout (default 10)
        * app_start_retry (default .90)
        * exists_timeout (default .5)
        * exists_retry (default .3)
        * after_click_wait (default .09)
        * after_clickinput_wait (default .01)
        * after_menu_wait (default .05)
        * after_sendkeys_key_wait (default .01)
        * after_button_click_wait (default 0)
        * before_closeclick_wait (default .1)
        * closeclick_retry (default .05)
        * closeclick_dialog_close_wait (default .05)
        * after_closeclick_wait (default .2)
        * after_windowclose_timeout (default 2)
        * after_windowclose_retry (default .5)
        * after_setfocus_wait (default .06)
        * after_setcursorpos_wait (default .01)
        * sendmessagetimeout_timeout (default .001)
        * after_tabselect_wait (default .01)
        * after_listviewselect_wait (default .01)
        * after_listviewcheck_wait default(.001)
        * after_treeviewselect_wait default(.001)
        * after_toobarpressbutton_wait default(.01)
        * after_updownchange_wait default(.001)
        * after_movewindow_wait default(0)
        * after_buttoncheck_wait default(0)
        * after_comboselect_wait default(0)
        * after_listboxselect_wait default(0)
        * after_listboxfocuschange_wait default(0)
        * after_editsetedittext_wait default(0)
        * after_editselect_wait default(0)
        """
        timeout_types = ["window_find_timeout", "window_find_retry", "app_start_timeout", "app_start_retry", "exists_timeout", 
        "exists_retry", "after_click_wait", "after_clickinput_wait", "after_menu_wait", "after_sendkeys_key_wait", 
        "after_button_click_wait", "before_closeclick_wait", "closeclick_retry", "closeclick_dialog_close_wait", "after_closeclick_wait",
        "after_windowclose_timeout", "after_windowclose_retry", "after_setfocus_wait", "after_setcursorpos_wait", 
        "sendmessagetimeout_timeout", "after_tabselect_wait", "after_listviewselect_wait", "after_listviewcheck_wait", 
        "after_treeviewselect_wait", "after_toobarpressbutton_wait", "after_updownchange_wait", "after_movewindow_wait", 
        "after_buttoncheck_wait", "after_comboselect_wait", "after_listboxselect_wait", "after_listboxfocuschange_wait",
        "after_editsetedittext_wait", "after_editselect_wait", "default"]
        
        if timeout_type not in timeout_types:
            raise ValueError, str(timeout_type + " is not one of the valid timeout types.")
        
        if timeout_type == "default":
            if new_timeout_time == "default":
                pywinauto.timings.Timings.Defaults()
            elif new_timeout_time == "fast":
                pywinauto.timings.Timings.Fast()
            elif new_timeout_time == "slow":
                pywinauto.timings.Timings.Slow()
            else:
                raise ValueError, str(new_timeout_time + ' needs to be either "fast", "slow" or "default"')
        else:
            # make sure we don't have anything other than a float or an int here.
            new_timeout_time = float(new_timeout_time)
            exec("pywinauto.timings.Timings." + timeout_type + " = " + str(new_timeout_time))
            
            print "changed " + timeout_type + " to " + str(new_timeout_time)
            return True
    
    def winDisconnectFromApplication(self):
        """
        Remove the current reference to an application and dialog.
        """
        self.app = None
        self.dlg = None
    
    def winGetExistingApplication(self, titleRegex):
        """
        Given a regex that indicates the window's title text, set the window as the current context.
        """
        # Reset the dialog and application contexts. We're selecting a new application, so niether of these are valid anymore.
        self.dlg = None
        self.app = None
        
        # TODO: need to put a sleep/wait loop here, right now it just fails if the window doesn't already exist.
        self.app = pwa.Application().connect(title_re = titleRegex)
        
    def winGetNewApplication(self, startCommand):
        """
        Given a command, execute it and return the identifier for the window it started.
        """
        # Reset the dialog and application contexts. We're selecting a new application, so niether of these are valid anymore.
        self.dlg = None
        self.app = None
        try:
            self.app = pwa.Application().start(startCommand)
        except pwa.AppStartError:
            print 'could not start the application "' + startCommand + '"'
            raise
        # Set the dialog back to nothing. We selected a new application, of course the dialog is nothing.
        
    def winGetDialogFromRegex(self, regex):
        """
        Given a regex, set the dialog who's title matches (in the current application) to the current context.
        """
        # TODO: make sure an app is selected first. Raise an error if not.
        if self.app:
            try:
                self.dlg = self.app.window_(title_re = regex)
                self.dlg.DrawOutline()
            except:
                print 'could not find the application matching "' + regex + '"'
        else:
            print 'No application currently selected. Searching for an application matching "' + regex + '"'
            try:
                self.app = pwa.Application().connect(title_re = regex)
            except:
                print 'Could not find application matching "' + regex + '" while searching for a dialog. No application was previously selected.'
                raise
            print 'Found an application matching "' + regex + '". Set this application to the current context.'
            print 'Searching for a matching dialog ("' + regex + '")'
            try:
                self.dlg = self.app[title]
                self.dlg.DrawOutline()
            except:
                print 'dialog not found matching "' + regex + '"'
                raise
        
        
    def winGetDialog(self, title):
        """
        Given an exact title, set the dialog matching it (in the current application) to the current context.
        If no application is selected currently, attempt to match both the application and dialog to this title.
        """
        # make sure there's an app selected. If there isn't, try to get an app matching the dialog name.
        if self.app:
            try:
                self.dlg = self.app[title]
                self.dlg.DrawOutline()
            except:
                print 'could not find a dialog with the title "' + title + '" associated with the current application'
                raise
        else:
            print 'No application currently selected. Searching for an application with the title "' + title + '"'
            try:
                self.app = pwa.Application().connect(title_re = title)
            except:
                print 'Could not find application with the title "' + title + '" while searching for a dialog with that title. No application was previously selected.'
                raise
            print 'Found an application with the title "' + title + '". Set this application to the current context.'
            print 'Searching for a dialog with the same title. ("' + title + '")'
            try:
                self.dlg = self.app[title]
                self.dlg.DrawOutline()
            except:
                print 'dialog not found with the title "' + title + '"'
                raise

    def winOutlineDialog(self):
        """
        Draw an outline around the current dialog
        """
        # Verify that we have an app and dialog selected.
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        
    
    def winMenuSelect(self, menulocation):
        """
        Given a menu location, select that menu item. The menu location should be given in this form: "Edit -> Replace" or "File -> Save As"
        Spaces are not important in this form, so "File->SaveAs" is also acceptable.
        
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        # TODO: Should I catch an error here? What if I specify a menu item that doesn't exist?
        self.dlg.MenuSelect(menulocation)
        
    def winGetWindowText(self):
        """
        Get the text of the currently selected dialog.
        Quite a few controls have other text that is visible, for example Edit controls usually have an empty string for WindowText 
        but still have text displayed in the edit window.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg.WindowText()
    
    def winGetControlText(self, control):
        """
        Get the text contained within a control on the current dialog.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].WindowText()
        
    def winGetNumberOfChildren(self, control):
        """
        Given a control on the current dialog, return the number of children of that control.
        IE, in a combo box, return the number of options. In a tab set, return the number of tabs.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
            
        return self.dlg[control].ControlCount()
    
    def winControlIsActive(self, control):
        """
        Given a control on the current dialog, assert that it is visible and enabled. If not, throw an error.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].VerifyActionable()
    
    def winControlIsEnabled(self, control):
        """
        Given a control on the current dialog, assert that it is enabled. If not, throw an error.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].VerifyEnabled()
        
    def winControlIsVisible(self, control):
        """
        Given a control on the current dialog, assert that it is visible. If not, throw an error.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].VerifyVisible()
    
    def winClick(self, control):
        """
        Send a click event to a control.
        
        This method sends WM_* messages to the control, to do a more 'realistic' mouse click use "win Real Click" which uses SendInput() API to perform the click.
        This method does not require that the control be visible on the screen (i.e. is can be hidden beneath another window and it will still work.)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Click()
    
    def winRealClick(self, control):
        """
        Move the mouse to the specified control, and click on it. DON'T MOVE THE MOUSE while using this action.
        
        This is different from Click in that it requires the control to be visible on the screen but performs a more realistic 'click' simulation.
        This method is also vulnerable if the mouse if moved by the user as that could easily move the mouse off the control before the Click has finished.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].ClickInput()
    
    def winDoubleClick(self, control):
        """
        Send a double click event to a control.
        
        This method sends WM_* messages to the control, to do a more 'realistic' mouse click use "win Real Double Click" which uses SendInput() API to perform the click.
        This method does not require that the control be visible on the screen (i.e. is can be hidden beneath another window and it will still work.)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].DoubleClick()
    
    def winRealDoubleClick(self, control):
        """
        Move the mouse to the specified control, and double click on it. DON'T MOVE THE MOUSE while using this action.
        
        This is different from Double Click in that it requires the control to be visible on the screen but performs a more realistic 'doubleclick' simulation.
        This method is also vulnerable if the mouse if moved by the user as that could easily move the mouse off the control before the doubleclick has finished.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].DoubleClickInput()
    
    def winRightClick(self, control):
        """
        Send a right click event to a control.
        
        This method sends WM_* messages to the control, to do a more 'realistic' mouse click use "win Real Right Click" which uses SendInput() API to perform the click.
        This method does not require that the control be visible on the screen (i.e. is can be hidden beneath another window and it will still work.)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].RightClick()
    
    def winRealRightClick(self, control):
        """
        Move the mouse to the specified control, and right click on it. DON'T MOVE THE MOUSE while using this action.
        
        This is different from Right Click in that it requires the control to be visible on the screen but performs a more realistic 'right click' simulation.
        This method is also vulnerable if the mouse if moved by the user as that could easily move the mouse off the control before the right click has finished.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].RightClickInput()
    
    def winDragMouse(self, control, press_x, press_y, release_x, release_y, button='left'):
        """
        Press, move and release the mouse button specified by "button" (left by default).
        The coordinates to press the mouse button at are x and y for "press_x" and "press_y" respectively.
        The coordinates to release the mouse button at are x and y for "release_x" and "release_y" respectively.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].DragMouse(button=button, press_coords=(press_x, press_y), release_coords=(release_x, release_y))
    
    def winTypeKeys(self, control, keys):
        """
        Type keyboard keys into the control.
        
        For how to do special characters, and other functionality above and beyond, check the sendkeys module in python.
        http://www.rutherfurd.net/python/sendkeys/
        The parameters for sendkeys used are: (pause=0.05, with_spaces=True, with_tabs=True, with_newlines=True, turn_off_numlock=True)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].TypeKeys(keys, pause=0.05, with_spaces=True, with_tabs=True, with_newlines=True, turn_off_numlock=True)
    
    def winCloseWindow(self):
        """
        Close the selected dialog
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg.Close()
    
    def winMaximizeWindow(self):
        """
        Maximize the selected dialog
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg.Maximize()
    
    def winMinimizeWindow(self):
        """
        Maximize the selected dialog
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg.Minimize()
    
    def winRestoreWindow(self):
        """
        Maximize the selected dialog
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg.Restore()
    
    def winSetWindowFocus(self):
        """
        Sets the current focus to the currently selected window.
        This will bring the window to the foreground if neccesary.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg.SetFocus()
    
    def winSetFocus(self, control):
        """
        Sets the current focus to the specified control.
        This will bring the window to the foreground if neccesary.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].SetFocus()
    
    def winScroll(self, control, direction, amount, count=1):
        """
        direction can be any of "up", "down", "left", "right" 
        amount can be one of "line", "page", "end" 
        count (optional) the number of times to scroll
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Scroll(direction, amount, count)
    
    def winControlHasFocus(self, control):
        """
        ### NOT COMPLETE - DO NOT USE ###
        Assert that the specified control has focus.
        """
        # TODO: Do this
        pass
    
    def winControlIsCheckBox(self, control):
        """
        Assert that the specified control is a check box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].FriendlyClassName == "CheckBox")
    
    def winControlIsButton(self, control):
        """
        Assert that the specified control is a button
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].FriendlyClassName == "Button")
    
    def winControlIsRadioButton(self, control):
        """
        Assert that the specified control is a check box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].FriendlyClassName == "RadioButton")
    
    def winControlIsGroupBox(self, control):
        """
        Assert that the specified control is a check box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].FriendlyClassName == "GroupBox")
    
    def winControlIsChecked(self, control):
        """
        Assert that the specified control is checked (checkbox, radio, etc.)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].GetCheckState() == 1)
    
    def winControlIsChecked(self, control):
        """
        Assert that the specified control is checked (checkbox, radio, etc.)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].GetCheckState() == 1)
    
    def winControlIsUnChecked(self, control):
        """
        Assert that the specified control is unchecked (checkbox, radio, etc.)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].GetCheckState() == 0)
    
    def winControlIsIndeterminate(self, control):
        """
        Assert that the specified control is in an indeterminate state (checkbox is partially checked)
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].GetCheckState() == 2)

    def winSetCheckboxToChecked(self, control):
        """
        Set the specified checkbox's state to checked.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Check()
    
    def winSetCheckboxToUnChecked(self, control):
        """
        Set the specified checkbox's state to unchecked.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].UnCheck()
    
    def winSetCheckboxToIndeterminate(self, control):
        """
        Set the specified checkbox's state to unchecked.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].SetCheckIndeterminate()
    
    def winGetComboBoxItems(self, control):
        """
        Given a control name in the current dialog, pull a pipe delimited string of all the valid items in that combo box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return "|".join(self.dlg[control].ItemTexts())
    
    def winGetComboBoxItemCount(self, control):
        """
        Get a count of the items in a combo box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].ItemCount() + 1 # This returns a number starting count at 0
    
    def winGetComboBoxSelectedIndex(self, control):
        """
        Get the selected index of a combo box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].SelectedIndex()
    
    def winGetComboBoxSelectedValue(self, control):
        """
        Get the selected value's text of a combo box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        # Texts returns the items in a combo box, with the first one being the selected item.
        return self.dlg[control].Texts()[0]
    
    def winComboBoxSelectIndex(self, control, value):
        """
        Select an item in the combo box. Value is an integer to the index of the item in the combo box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(int(value))
        
    def winComboBoxSelectValue(self, control, value):
        """
        Select an item in the combo box. Value is a string with the exact text of the item to select in the combo box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(value)
    
    def winGetEditBoxLineCount(self, control):
        """
        Given an edit box control on the current dialog, return the number of lines in the edit box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].LineCount() + 1 # This returns a number starting count at 0
    
    def winGetEditBoxLineText(self, control, line_index):
        """
        Given an edit box control on the current dialog, and an int for the index of a line in that edit box, return that line's text.
        If you give this a line that doesn't exist, it returns an empty string.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].GetLine(line_index)
    
    def winGetEditBoxText(self, control):
        """
        Given an edit box control on the current dialog, return the text for that control.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].TextBlock()
    
    def winSetEditBoxText(self, control, textblock):
        """
        Given an edit box control on the current dialog, and a block of text, set the block to the text for that control.
        As this is windows vs linux, \\n won't represent a newline. \\r\\n is needed to represent a newline. This differs from sendkeys 
        because you are setting the control text directly vs typing it.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].SetEditText(textblock)
    
    def winGetListBoxItems(self, control):
        """
        Given a control name in the current dialog, pull a pipe delimited string of all the valid items in that list box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return "|".join(self.dlg[control].ItemTexts())
    
    def winGetListBoxItemCount(self, control):
        """
        Get a count of the items in a list box
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].ItemCount() + 1 # This returns a number starting count at 0
    
    def winGetListBoxSelectedIndex(self, control):
        """
        Get the selected indices of a list box. Returns a pipe delimited list of the index of each selected item.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        selected = []
        for i in self.dlg[control].SelectedIndices():
            selected.append(str(i))
        return "|".join(selected)
    
    def winGetListBoxSelectedValue(self, control):
        """
        Get the selected value's text from a list box. Returns a pipe delimited list of the text of each selected item.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        # get the texts for the values.
        texts = self.dlg[control].Texts()
        
        selected = []
        for i in self.dlg[control].SelectedIndices():
            # Select from the texts, the values of each selected item.
            selected.append(texts[i])
        return "|".join(selected)
    
    def winListBoxSelectIndex(self, control, value):
        """
        Select an item in the list box. Value is an integer to the index of the item in the list box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(int(value))
        
    def winListBoxSelectValue(self, control, value):
        """
        Select an item in the list box. Value is a string with the exact text of the item to select in the list box.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(value)
    
    def winListBoxDeselectAll(self, control):
        """
        Deselect all currently selected items in a list box.
        Not 100% sure this works. Please test and let me know either way.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        for i in self.dlg[control].SelectedIndices():
            # Select from the texts, the values of each selected item.
            self.dlg[control].Select(i)

    def winGetListViewColumnCount(self, control):
        """
        Get a count of the columns in a listview control
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].ColumnCount() + 1 # This returns a number starting count at 0
    
    def winGetListViewItemCount(self, control):
        """
        Get a count of the items in a listview control
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].ItemCount() + 1 # This returns a number starting count at 0
    
    def winListViewHeaderText(self, control):
        """
        Given a listview control, return a pipe delimited list of the header text associated with the columns
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        texts = []
        for i in self.dlg[control].Columns():
            texts.append(i["text"])
        return "|".join(texts)
    
    def winListViewGetSelectedCount(self, control):
        """
        Get the number of selected items in the listview
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].GetSelectedCount() + 1 # This returns a number starting count at 0
        
    def winListViewIndexIsSelected(self, control, index):
        """
        Assert that the item specified by the index is selected
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].IsSelected(index))
    
    def winListViewIndexIsNotSelected(self, control, index):
        """
        Assert that the item specified by the index is not selected
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].IsSelected(index) == False)
    
    def winListViewSelectIndex(self, control, index):
        """
        Select an item specified by the index.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(index)
    
    def winListViewDeselectIndex(self, control, index):
        """
        Deselect an item specified by the index.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Deselect(index)

    def winListViewIndexIsChecked(self, control, index):
        """
        Assert that the item specified by the index is checked
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].IsChecked(index))
    
    def winListViewIndexIsNotChecked(self, control, index):
        """
        Assert that the item specified by the index is not checked
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        assert(self.dlg[control].IsChecked(index) == False)
    
    def winListViewCheckIndex(self, control, index):
        """
        Check an item specified by the index.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Check(index)
    
    def winListViewUncheckIndex(self, control, index):
        """
        Uncheck an item specified by the index.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].UnCheck(index)
    
    def winGetStatusBarPartCount(self, control):
        """
        Return the number of "parts" associated with a status bar on the current dialog
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].PartCount() + 1 # This returns a number starting count at 0
    
    def winGetStatusBarPartText(self, control, index):
        """
        Given a status bar control, and the index of the part in that status bar, return the text contained
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].GetPartText(index)
        
    def winGetStatusBarText(self, control):
        """
        Given a status bar control, return the text contained in it's parts, in a pipe delimited string.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return "|".join(self.dlg[control].Texts())
    
    def winGetTabCount(self, control):
        """
        Given a tab control, return the number of tabs in that control.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].TabCount() + 1 # This returns a number starting count at 0
    
    def winGetSelectedTabIndex(self, control):
        """
        Given a tab control, return the index of the selected tab.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].GetSelectedTab()
    
    def winGetTabText(self, control, index):
        """
        Given a tab control, and an index, return the text associated with the tab specified by the index
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].GetTabText(index)
    
    def winGetAllTabTexts(self, control, index):
        """
        Given a tab control, return the text associated with all tabs in that control, in a pipe delimited string
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return "|".join(self.dlg[control].Texts())
    
    def winSelectTabByText(self, control, text):
        """
        Given a tab control, and the text of a tab in it, select that tab.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(str(text))
        
    def winSelectTabByIndex(self, control, index):
        """
        Given a tab control, and the text of a tab in it, select that tab.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].Select(int(index))
    
    def winGetToolbarButtonCount(self, control):
        """
        Given a toolbar control, return the number of buttons on the toolbar
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].ButtonCount() + 1 # This returns a number starting count at 0
    
    def winGetToolbarButtonText(self, control, index):
        """
        Given an index of a button on the specified toolbar control, return the button's text
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        return self.dlg[control].GetButton(index).text.value
        
    def winClickToolbarButton(self, control, text):
        """
        Given the text of a button on the specified toolbar control, press that button
        Not 100% sure this works. It's an undocumented feature in the pywinauto library...
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        self.dlg[control].PressButton(text)
    
    def winGetTreeText(self, control):
        """
        Return all text for a tree in a pipe delimited string
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        "|".join(self.dlg[control].Texts())
        
    def winClickTreeElement(self, control, path):
        """
        Click a treeview control element by the path within the tree.
        The path should take the same form as a menu, where -> delimits the nodes.
        For example "Tree->Node2->Subnode1" would specify Subnode1 on the tree below
        
        + Tree
        ----+ Node1
        ----+ Node2
        --------+ Subnode1
        ----+ Node3
        --------+ Subnode2
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        path = '\\' + path.replace('->', '\\')
        
        self.dlg[control].GetItem(path).Click()
    
    def winRightClickTreeElement(self, control, path):
        """
        Right Click a treeview control element by the path within the tree.
        The path should take the same form as a menu, where -> delimits the nodes.
        For example "Tree->Node2->Subnode1" would specify Subnode1 on the tree below
        
        + Tree
        ----+ Node1
        ----+ Node2
        --------+ Subnode1
        ----+ Node3
        --------+ Subnode2
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        path = '\\' + path.replace('->', '\\')
        
        self.dlg[control].GetItem(path).Click(button='right')
    
    def winDoubleClickTreeElement(self, control, path):
        """
        Double Click a treeview control element by the path within the tree.
        The path should take the same form as a menu, where -> delimits the nodes.
        For example "Tree->Node2->Subnode1" would specify Subnode1 on the tree below
        
        + Tree
        ----+ Node1
        ----+ Node2
        --------+ Subnode1
        ----+ Node3
        --------+ Subnode2
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        path = '\\' + path.replace('->', '\\')
        
        self.dlg[control].GetItem(path).Click(double=True)
    
    def winExpandTreeElement(self, control, path):
        """
        Expand a treeview control element by the path within the tree.
        The path should take the same form as a menu, where -> delimits the nodes.
        For example "Tree->Node2->Subnode1" would specify Subnode1 on the tree below
        
        + Tree
        ----+ Node1
        ----+ Node2
        --------+ Subnode1
        ----+ Node3
        --------+ Subnode2
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        
        path = '\\' + path.replace('->', '\\')
        
        self.dlg[control].GetItem(path).Expand()
    
    def winPopupMenuSelect(self, menulocation):
        """
        Given a popup menu option, select that menu item. The menu location should be given in this form: "Edit -> Replace" or "File -> Save As"
        Spaces are not important in this form, so "File->SaveAs" is also acceptable.
        """
        if self.app == None:
            raise UnboundLocalError, "There is no application context currently set"
        if self.dlg == None:
            raise UnboundLocalError, "There is no dialog context currently set"
        # TODO: Should I catch an error here? What if I specify a menu item that doesn't exist?
        self.app.PopupMenu.MenuSelect(menulocation)
        
