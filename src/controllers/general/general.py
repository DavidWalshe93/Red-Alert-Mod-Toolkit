"""
Author:     David Walshe
Date:       06 July 2020
"""

from src.controllers.general.economy import EconomyController
from src.controllers.general.combat import CombatController
from src.model.models.general import GeneralDefaults, GeneralCustom


class GeneralController(EconomyController, CombatController):

    def __init__(self, *args, **kwargs):
        """
        Controls updates to the GUI elements via the database.
        """
        super().__init__(*args, *kwargs)

        self.populate_data()
        # self.bind_controller_slots()

    # def bind_controller_slots(self):
    #     self.view.bailCountSpinBox.valueChanged.connect(self.update_db_on_change)
    #     # self.view.buildSpeedSpinBox.valueChanged.connect(self.u)

    def populate_data(self, result=None) -> None:
        table = GeneralCustom

        # There is only one record in this table.
        result = self.model.query_first(table)
        self.bail_count = result
        self.build_speed = result
        self.gem_value = result
        self.gold_value = result
        self.growth_rate = result
        self.ore_grows = result
        self.ore_spreads = result
        self.ore_truck_rate = result
        self.separate_aircraft = result
        self.survivor_rate = result

    @property
    def table(self):
        return self.get_custom_table()

    @property
    def tables(self):
        return self.get_custom_table(), self.get_default_table()

    def get_custom_table(self, *args):
        return GeneralCustom

    def get_default_table(self, *args):
        return GeneralDefaults
