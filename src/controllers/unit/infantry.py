"""
Author:     David Walshe
Date:       03 July 2020
"""
from abc import ABC

from src.controllers.utils import set_checked, is_checked
from src.controllers.unit.unit import UnitController
from src.model.models.units.infantry import Infantry


class InfantryController(UnitController, ABC):

    def populate_data(self, result: Infantry):
        """
        Populates the data from the database into the view.

        :param result: The database query result.
        """
        super().populate_data(result)
        if isinstance(result, Infantry):
            self.c4 = result
            self.fraidycat = result
            self.infiltrate = result
            self.is_canine = result

    @property
    def c4(self):
        return is_checked(self.view.c4checkBox)

    @c4.setter
    def c4(self, value: Infantry):
        self.view.c4CheckBox.setCheckState(set_checked(value.C4))

    @property
    def fraidycat(self):
        return is_checked(self.view.fraidycatCheckBox)

    @fraidycat.setter
    def fraidycat(self, value: Infantry):
        self.view.fraidycatCheckBox.setCheckState(set_checked(value.Fraidycat))

    @property
    def infiltrate(self):
        return is_checked(self.view.infiltrateCheckBox)

    @infiltrate.setter
    def infiltrate(self, value: Infantry):
        self.view.infiltrateCheckBox.setCheckState(set_checked(value.Infiltrate))

    @property
    def is_canine(self):
        return is_checked(self.view.isCanineCheckBox)

    @is_canine.setter
    def is_canine(self, value: Infantry):
        self.view.isCanineCheckBox.setCheckState(set_checked(value.IsCanine))
