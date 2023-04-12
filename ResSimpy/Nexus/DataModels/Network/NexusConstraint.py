from dataclasses import dataclass
from typing import Optional

from ResSimpy.Constraint import Constraint
from ResSimpy.Nexus.NexusEnums.UnitsEnum import UnitSystem
from ResSimpy.Utils import to_dict_generic
from ResSimpy.Utils.generic_repr import generic_repr


@dataclass
class NexusConstraint(Constraint):
    """
    Attributes:
        name (str): name of the well (NAME)
        max_surface_oil_rate (float): max surface oil rate (QOSMAX)
        max_surface_gas_rate (float): max surface gas rate (QGSMAX)
        max_surface_water_rate (float): max surface (QWSMAX)
        max_surface_liquid_rate (float): max surface liquid rate (QLIQSMAX)
        max_hc_molar_rate (float): Max hc molar rate (QMHCMAX)
        max_reverse_surface_oil_rate (float): max reverse surface oil rate (QOSMAX-)
        max_reverse_surface_gas_rate (float): max reverse surface gas rate (QGSMAX-)
        max_reverse_surface_water_rate (float): max reverse surface water rate (QWSMAX-)
        max_reverse_surface_liquid_rate (float): max reverse surface liquid rate (QLIQSMAX-)
        max_reservoir_oil_rate (float): max reservoir oil rate (QOMAX)
        max_reservoir_gas_rate (float): max reservoir gas rate (QGMAX)
        max_reservoir_water_rate (float): max reservoir water rate (QWMAX)
        max_reservoir_liquid_rate (float): max reservoir liquid rate (QLIQMAX)
        max_reservoir_total_fluids_rate (float): max reservoir total fluids rate (QALLMAX)
        max_reservoir_hc_rate (float): max reservoir hc rate (QHCMAX)
        max_reverse_reservoir_oil_rate (float): max reverse reservoir oil rate (QOMAX-)
        max_reverse_reservoir_gas_rate (float): max reverse reservoir gas rate (QGMAX-)
        max_reverse_reservoir_water_rate (float): max reverse reservoir water rate (QWMAX-)
        max_reverse_reservoir_liquid_rate (float): max reverse reservoir liquid rate (QLIQMAX-)
        max_reverse_reservoir_total_fluids_rate (float): max reverse reservoir total fluids rate (QALLMAX-)
        max_reverse_reservoir_hc_rate (float): max reverse reservoir hc rate (QHCMAX-)
        min_pressure (float): min pressure (PMIN)
        max_pressure (float): max pressure (PMAX)
        max_wag_water_pressure (float): max wag water pressure (PWMAX)
        max_wag_gas_pressure (float): max wag gas pressure (PGMAX)
        bottom_hole_pressure (float): bottom hole pressure (BHP)
        tubing_head_pressure (float): tubing head pressure (THP)
        min_surface_oil_rate (float): min surface oil rate (QOSMIN)
        min_surface_gas_rate (float): min surface gas rate (QGSMIN)
        min_surface_water_rate (float): min surface water rate (QWSMIN)
        min_surface_liquid_rate (float): min surface liquid rate (QLIQSMIN)
        min_reservoir_oil_rate (float): min reservoir oil rate (QOMIN)
        min_reservoir_gas_rate (float): min reservoir gas rate (QGMIN)
        min_reservoir_water_rate (float): min reservoir water rate (QWMIN)
        min_reservoir_liquid_rate (float): min reservoir liquid rate (QLIQMIN)
        min_reservoir_total_fluids_rate (float): min reservoir total fluids rate (QALLMIN)
        min_reservoir_hc_rate (float): min reservoir hc rate (QHCMIN)
        min_reservoir_oil_rate (float): min reservoir oil rate (QOSMIN-)
        min_reservoir_gas_rate (float): min reservoir gas rate (QGSMIN-)
        min_reservoir_water_rate (float): min reservoir water rate (QWSMIN-)
        min_reservoir_liquid_rate (float): min reservoir liquid rate (QLIQSMIN-)
        min_reverse_reservoir_oil_rate (float): min reverse reservoir oil rate (QOMIN-)
        min_reverse_reservoir_gas_rate (float): min reverse reservoir gas rate (QGMIN-)
        min_reverse_reservoir_water_rate (float): min reverse reservoir water rate (QWMIN-)
        min_reverse_reservoir_liquid_rate (float): min reverse reservoir liquid rate (QLIQMIN-)
        min_reverse_reservoir_total_fluids_rate (float): min reverse reservoir total fluids rate (QALLMIN-)
        min_reverse_reservoir_hc_rate (float): min reverse reservoir hc rate (QHCMIN-)
        max_watercut (float): max watercut (WCUTMAX)
        max_watercut_plug (float): max watercut plug (WCUTPLUG)
        max_watercut_plugplus (float): max watercut plugplus (WCUTPLUGPLUS)
        max_watercut_perf (float): max watercut perf (WCUTPERF)
        max_watercut_perfplus (float): max watercut perfplus (WCUTPERFPLUS)
        max_wor (float): max wor (WORMAX)
        max_wor_plug (float): max wor plug (WORPLUG)
        max_wor_plug_plus (float): max wor plug plus (WORPLUGPLUS)
        max_wor_perf (float): max wor perf (WORPERF)
        max_wor_perfplus (float): max wor perfplus (WORPERFPLUS)
        max_gor (float): max gor (GORMAX)
        max_gor_plug (float): max gor plug (GORPLUG)
        max_gor_plug_plus (float): max gor plug plus (GORPLUGPLUS)
        max_gor_perf (float): max gor perf (GORPERF)
        max_gor_perfplus (float): max gor perfplus (GORPERFPLUS)
        max_lgr (float): max lgr (LGRMAX)
        max_lgr_plug (float): max lgr plug (LGRPLUG)
        max_lgr_plug_plus (float): max lgr plug plus (LGRPLUGPLUS)
        max_lgr_perf (float): max lgr perf (LGRPERF)
        max_lgr_perfplus (float): max lgr perfplus (LGRPERFPLUS)
        max_cum_gas_prod (float): max cum gas prod (CGLIM)
        max_cum_water_prod (float): max cum water prod (CWLIM)
        max_cum_oil_prod (float): max cum oil prod (COLIM)
    """
    name: Optional[str] = None
    max_surface_oil_rate: Optional[float] = None
    max_surface_gas_rate: Optional[float] = None
    max_surface_water_rate: Optional[float] = None
    max_surface_liquid_rate: Optional[float] = None
    max_hc_molar_rate: Optional[float] = None
    max_reverse_surface_oil_rate: Optional[float] = None
    max_reverse_surface_gas_rate: Optional[float] = None
    max_reverse_surface_water_rate: Optional[float] = None
    max_reverse_surface_liquid_rate: Optional[float] = None
    max_reservoir_oil_rate: Optional[float] = None
    max_reservoir_gas_rate: Optional[float] = None
    max_reservoir_water_rate: Optional[float] = None
    max_reservoir_liquid_rate: Optional[float] = None
    max_reservoir_total_fluids_rate: Optional[float] = None
    max_reservoir_hc_rate: Optional[float] = None
    max_reverse_reservoir_oil_rate: Optional[float] = None
    max_reverse_reservoir_gas_rate: Optional[float] = None
    max_reverse_reservoir_water_rate: Optional[float] = None
    max_reverse_reservoir_liquid_rate: Optional[float] = None
    max_reverse_reservoir_total_fluids_rate: Optional[float] = None
    max_reverse_reservoir_hc_rate: Optional[float] = None
    min_pressure: Optional[float] = None
    max_pressure: Optional[float] = None
    max_wag_water_pressure: Optional[float] = None
    max_wag_gas_pressure: Optional[float] = None
    bottom_hole_pressure: Optional[float] = None
    tubing_head_pressure: Optional[float] = None
    min_surface_oil_rate: Optional[float] = None
    min_surface_gas_rate: Optional[float] = None
    min_surface_water_rate: Optional[float] = None
    min_surface_liquid_rate: Optional[float] = None
    min_reservoir_oil_rate: Optional[float] = None
    min_reservoir_gas_rate: Optional[float] = None
    min_reservoir_water_rate: Optional[float] = None
    min_reservoir_liquid_rate: Optional[float] = None
    min_reservoir_total_fluids_rate: Optional[float] = None
    min_reservoir_hc_rate: Optional[float] = None
    min_reverse_reservoir_oil_rate: Optional[float] = None
    min_reverse_reservoir_gas_rate: Optional[float] = None
    min_reverse_reservoir_water_rate: Optional[float] = None
    min_reverse_reservoir_liquid_rate: Optional[float] = None
    min_reverse_reservoir_total_fluids_rate: Optional[float] = None
    min_reverse_reservoir_hc_rate: Optional[float] = None
    max_watercut: Optional[float] = None
    max_watercut_plug: Optional[float] = None
    max_watercut_plugplus: Optional[float] = None
    max_watercut_perf: Optional[float] = None
    max_watercut_perfplus: Optional[float] = None
    max_wor: Optional[float] = None
    max_wor_plug: Optional[float] = None
    max_wor_plug_plus: Optional[float] = None
    max_wor_perf: Optional[float] = None
    max_wor_perfplus: Optional[float] = None
    max_gor: Optional[float] = None
    max_gor_plug: Optional[float] = None
    max_gor_plug_plus: Optional[float] = None
    max_gor_perf: Optional[float] = None
    max_gor_perfplus: Optional[float] = None
    max_lgr: Optional[float] = None
    max_lgr_plug: Optional[float] = None
    max_lgr_plug_plus: Optional[float] = None
    max_lgr_perf: Optional[float] = None
    max_lgr_perfplus: Optional[float] = None
    max_cum_gas_prod: Optional[float] = None
    max_cum_water_prod: Optional[float] = None
    max_cum_oil_prod: Optional[float] = None

    def __init__(self, properties_dict: dict[str, None | int | str | float | UnitSystem]):
        super().__init__()
        for key, prop in properties_dict.items():
            self.__setattr__(key, prop)

    @staticmethod
    def get_nexus_mapping() -> dict[str, tuple[str, type]]:
        """gets the mapping of nexus keywords to attribute definitions"""
        nexus_mapping = {
            'NAME': ('name', str),
            'QOSMAX': ('max_surface_oil_rate', float),
            'QGSMAX': ('max_surface_gas_rate', float),
            'QWSMAX': ('max_surface_water_rate', float),
            'QLIQSMAX': ('max_surface_liquid_rate', float),
            'QMHCMAX': ('max_hc_molar_rate', float),

            'QOSMAX-': ('max_reverse_surface_oil_rate', float),
            'QGSMAX-': ('max_reverse_surface_gas_rate', float),
            'QWSMAX-': ('max_reverse_surface_water_rate', float),
            'QLIQSMAX-': ('max_reverse_surface_liquid_rate', float),
            'QOMAX': ('max_reservoir_oil_rate', float),
            'QGMAX': ('max_reservoir_gas_rate', float),
            'QWMAX': ('max_reservoir_water_rate', float),
            'QLIQMAX': ('max_reservoir_liquid_rate', float),
            'QALLMAX': ('max_reservoir_total_fluids_rate', float),
            'QHCMAX': ('max_reservoir_hc_rate', float),
            'QOMAX-': ('max_reverse_reservoir_oil_rate', float),
            'QGMAX-': ('max_reverse_reservoir_gas_rate', float),
            'QWMAX-': ('max_reverse_reservoir_water_rate', float),
            'QLIQMAX-': ('max_reverse_reservoir_liquid_rate', float),
            'QALLMAX-': ('max_reverse_reservoir_total_fluids_rate', float),
            'QHCMAX-': ('max_reverse_reservoir_hc_rate', float),

            'PMIN': ('min_pressure', float),
            'PMAX': ('max_pressure', float),
            'PWMAX': ('max_wag_water_pressure', float),
            'PGMAX': ('max_wag_gas_pressure', float),
            'BHP': ('bottom_hole_pressure', float),
            'THP': ('tubing_head_pressure', float),

            'QOSMIN': ('min_surface_oil_rate', float),
            'QGSMIN': ('min_surface_gas_rate', float),
            'QWSMIN': ('min_surface_water_rate', float),
            'QLIQSMIN': ('min_surface_liquid_rate', float),
            'QOMIN': ('min_reservoir_oil_rate', float),
            'QGMIN': ('min_reservoir_gas_rate', float),
            'QWMIN': ('min_reservoir_water_rate', float),
            'QLIQMIN': ('min_reservoir_liquid_rate', float),
            'QALLMIN': ('min_reservoir_total_fluids_rate', float),
            'QHCMIN': ('min_reservoir_hc_rate', float),
            'QOSMIN-': ('min_reservoir_oil_rate', float),
            'QGSMIN-': ('min_reservoir_gas_rate', float),
            'QWSMIN-': ('min_reservoir_water_rate', float),
            'QLIQSMIN-': ('min_reservoir_liquid_rate', float),
            'QOMIN-': ('min_reverse_reservoir_oil_rate', float),
            'QGMIN-': ('min_reverse_reservoir_gas_rate', float),
            'QWMIN-': ('min_reverse_reservoir_water_rate', float),
            'QLIQMIN-': ('min_reverse_reservoir_liquid_rate', float),
            'QALLMIN-': ('min_reverse_reservoir_total_fluids_rate', float),
            'QHCMIN-': ('min_reverse_reservoir_hc_rate', float),

            'WCUTMAX': ('max_watercut', float),
            'WCUTPLUG': ('max_watercut_plug', float),
            'WCUTPLUGPLUS': ('max_watercut_plugplus', float),
            'WCUTPERF': ('max_watercut_perf', float),
            'WCUTPERFPLUS': ('max_watercut_perfplus', float),
            'WORMAX': ('max_wor', float),
            'WORPLUG': ('max_wor_plug', float),
            'WORPLUGPLUS': ('max_wor_plug_plus', float),
            'WORPERF': ('max_wor_perf', float),
            'WORPERFPLUS': ('max_wor_perfplus', float),
            'GORMAX': ('max_gor', float),
            'GORPLUG': ('max_gor_plug', float),
            'GORPLUGPLUS': ('max_gor_plug_plus', float),
            'GORPERF': ('max_gor_perf', float),
            'GORPERFPLUS': ('max_gor_perfplus', float),
            'LGRMAX': ('max_lgr', float),
            'LGRPLUG': ('max_lgr_plug', float),
            'LGRPLUGPLUS': ('max_lgr_plug_plus', float),
            'LGRPERF': ('max_lgr_perf', float),
            'LGRPERFPLUS': ('max_lgr_perfplus', float),
            'CGLIM': ('max_cum_gas_prod', float),
            'CWLIM': ('max_cum_water_prod', float),
            'COLIM': ('max_cum_oil_prod', float),
        }
        return nexus_mapping

    def to_dict(self, keys_in_nexus_style: bool = False) -> dict[str, None | str | int | float]:
        """
            Returns a dictionary of the attributes of the Constraint
        Args:
            keys_in_nexus_style (bool): if True returns the key values in Nexus keywords, otherwise returns the \
                attribute name as stored by ressimpy

        Returns:
            a dictionary keyed by attributes and values as the value of the attribute
        """
        result_dict = to_dict_generic.to_dict(self, keys_in_nexus_style, add_date=True, add_units=True)
        return result_dict

    def update(self, new_data: dict[str, None | int | str | float | UnitSystem]):
        """Updates attributes in the object based on the dictionary provided"""
        for k, v in new_data.items():
            if v is not None:
                setattr(self, k, v)

    def __repr__(self):
        return generic_repr(self)