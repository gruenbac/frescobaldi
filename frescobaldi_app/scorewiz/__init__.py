# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2014 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
The Score Wizard.
"""


from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction

import actioncollection
import actioncollectionmanager
import icons
import plugin


class ScoreWizard(plugin.MainWindowPlugin):
    def __init__(self, mainwindow):
        self.actionCollection = ac = Actions()
        actioncollectionmanager.manager(mainwindow).addActionCollection(ac)
        ac.scorewizNew.triggered.connect(self.showNewDialog)
        ac.scorewizEdit.triggered.connect(self.showEditDialog)
        self._dlg = None

    def dialog(self):
        """Return the wizard dialog, creating it if necessary."""
        if self._dlg is None:
            from . import dialog
            self._dlg = dialog.ScoreWizardDialog(self.mainwindow())
        return self._dlg

    def showNewDialog(self):
        """Show the dialog for creating a new score."""
        self.dialog().show()

    def showEditDialog(self):
        """Show the dialog for editing an existing score."""
        self.dialog().show()
        self.dialog().readScore()


class Actions(actioncollection.ActionCollection):
    name = 'scorewiz'
    def createActions(self, parent=None):
        self.scorewizNew = QAction(parent)
        self.scorewizNew.setIcon(icons.get("tools-score-wizard"))
        self.scorewizNew.setShortcut(QKeySequence("Ctrl+Shift+N"))
        self.scorewizNew.setMenuRole(QAction.NoRole)

        self.scorewizEdit = QAction(parent)
        self.scorewizEdit.setIcon(icons.get("tools-score-wizard"))
        self.scorewizEdit.setMenuRole(QAction.NoRole)

    def translateUI(self):
        self.scorewizNew.setText(_("Score &Wizard..."))
        self.scorewizEdit.setText(_("Score S&etup Wizard..."))


