from datausa.database import db

from datausa.acs.abstract_models import BaseAcs1, BaseAcs5, GeoId, GeoId5, GeoId1
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData

metadata = MetaData(schema='acs')
AutomapBase = automap_base(bind=db.engine, metadata=metadata)

metadata_1yr = MetaData(schema='acs_1year')
AutomapBase_1yr = automap_base(bind=db.engine, metadata=metadata_1yr)

# 1 year

class Acs1_Yg(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = "yg"
    median_moe = 1

class Acs1_Yg_IncDist(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = "yg_income_distribution"
    median_moe = 2

class Acs1_Yg_PovertyRace(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_poverty_race'
    median_moe = 2

class Acs1_Yg_NatAge(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_nativity_age'
    median_moe = 1

class Acs1_Yg_Race(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_race'
    median_moe = 1

class Acs1_Yg_Conflict(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = "yg_conflict"
    median_moe = 2

class Acs1_Yg_PropertyValue(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_property_value'
    median_moe = 1

class Acs1_Yg_PropertyTax(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_property_tax'
    median_moe = 1

class Acs1_Yg_Vehicles(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_vehicles'
    median_moe = 1

class Acs1_Yg_TravelTime(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_travel_time'
    median_moe = 1

class Acs1_Yg_Transport(AutomapBase_1yr, BaseAcs1, GeoId1):
    __tablename__ = 'yg_transport'
    median_moe = 1

# 5 year

class Acs5_Yg(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = "yg"
    median_moe = 1

class Acs5_Yg_Conflict(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = "yg_conflict"
    median_moe = 2

class Acs5_Yg_Income(BaseAcs5, GeoId5):
    __tablename__ = "yg_income"
    median_moe = 1.2

class Acs5_Yg_IncDist(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = "yg_income_distribution"
    median_moe = 2

class Acs5_Yg_NatAge(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_nativity_age'
    median_moe = 1


class Acs5_Yg_Poverty(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_poverty'
    median_moe = 1


class Acs5_Yg_PropertyTax(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_property_tax'
    median_moe = 1


class Acs5_Yg_PropertyValue(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_property_value'
    median_moe = 1


class Acs5_Yg_Race(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_race'
    median_moe = 1


class Acs5_Yg_PovertyRace(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_poverty_race'
    median_moe = 2


class Acs5_Yg_Tenure(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_tenure'
    median_moe = 1


class Acs5_Yg_Transport(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_transport'
    median_moe = 1


class Acs5_Yg_TravelTime(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_travel_time'
    median_moe = 1


class Acs5_Yg_Vehicles(AutomapBase, BaseAcs5, GeoId5):
    __tablename__ = 'yg_vehicles'
    median_moe = 1

AutomapBase_1yr.prepare(db.engine, reflect=True)
AutomapBase.prepare(db.engine, reflect=True)
