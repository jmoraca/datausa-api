from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declared_attr
from datausa.core.exceptions import DataUSAException

from datausa.database import db
from datausa.attrs import consts
from datausa.core.models import BaseModel
from datausa.attrs.models import *
from datausa.attrs.consts import NATION, STATE, PUMA, ALL, GEO, COUNTY


def geo_sumlevel_filter(table, show_colname, sumlevel):
    sumlevel_codes = {NATION: "010", STATE: "040",
                      PUMA: "795"}
    if not sumlevel in sumlevel_codes:
        raise DataUSAException("Invalid sumlevel", sumlevel)
    start_code = sumlevel_codes[sumlevel]
    return table.geo.startswith(start_code)

class BasePums(db.Model, BaseModel):
    __abstract__ = True
    __table_args__ = {"schema": "pums_1year"}
    source_title = 'ACS PUMS 1-year Estimate'
    source_link = 'http://census.gov/programs-surveys/acs/technical-documentation/pums.html'

    num_records =  db.Column(db.Integer)

    @classmethod
    def gen_show_level_filters(cls, shows_and_levels):
        result = []
        for show_colname, sumlevel in shows_and_levels.items():
            if sumlevel != ALL:
                if show_colname == "geo":
                    filt = geo_sumlevel_filter(cls, show_colname, sumlevel)
                    result.append(filt)

        return result

    def __repr__(self):
        return '<{}>'.format(self.__class__)

class Personal(object):
    avg_age = db.Column(db.Float())
    avg_wage =  db.Column(db.Float())
    avg_hrs =  db.Column(db.Float())
    num_ppl =  db.Column(db.Integer())

    avg_age_moe = db.Column(db.Float())
    avg_wage_moe =  db.Column(db.Float())
    avg_hrs_moe = db.Column(db.Float())

    num_ppl_moe =  db.Column(db.Float())

class PersonalWithAge(object):
    avg_wage =  db.Column(db.Float())
    avg_hrs =  db.Column(db.Float())
    num_ppl =  db.Column(db.Integer())

    avg_wage_moe =  db.Column(db.Float())
    avg_hrs_moe = db.Column(db.Float())

    num_ppl_moe =  db.Column(db.Float())


class Year(object):
    @declared_attr
    def year(cls):
        return db.Column(db.Integer(), primary_key=True)

class GeoId(object):
    LEVELS = [NATION, STATE, PUMA, ALL]
    @classmethod
    def get_supported_levels(cls):
        return {GEO: GeoId.LEVELS}

    @classmethod
    def geo_filter(cls, level):
        if level == ALL:
            return True
        level_map = {NATION: "010", STATE: "040", PUMA: "795"}
        level_code = level_map[level]
        return cls.geo.startswith(level_code)

    @declared_attr
    def geo(cls):
        return db.Column(db.String(), db.ForeignKey(Geo.id), primary_key=True)

class CipId(object):
    @declared_attr
    def cip(cls):
        return db.Column(db.String(), db.ForeignKey(Cip.id), primary_key=True)

class DegreeId(object):
    @declared_attr
    def degree(cls):
        return db.Column(db.String(), db.ForeignKey(PumsDegree.id), primary_key=True)

class NaicsId(object):
    LEVELS = ["0", "1", "2", "all"]
    naics_level = db.Column(db.Integer())

    @declared_attr
    def naics(cls):
        return db.Column(db.String(), db.ForeignKey(PumsNaics.id), primary_key=True)

    @classmethod
    def naics_filter(cls, level):
        if level == consts.ALL:
            return True
        return cls.naics_level == level

class SocId(object):
    LEVELS = ["0", "1", "2", "3", "all"]
    soc_level = db.Column(db.Integer())

    @declared_attr
    def soc(cls):
        return db.Column(db.String(), db.ForeignKey(PumsSoc.id), primary_key=True)

    @classmethod
    def soc_filter(cls, level):
        if level == consts.ALL:
            return True
        return cls.soc_level == level

class WageId(object):
    @declared_attr
    def wage_bin(cls):
        return db.Column(db.String(), db.ForeignKey(PumsWage.id), primary_key=True)

class RaceId(object):
    @declared_attr
    def race(cls):
        return db.Column(db.String(), db.ForeignKey(PumsRace.id), primary_key=True)

class SexId(object):
    @declared_attr
    def sex(cls):
        return db.Column(db.String(), db.ForeignKey(PumsSex.id), primary_key=True)

class BirthplaceId(object):
    @declared_attr
    def birthplace(cls):
        return db.Column(db.String(), db.ForeignKey(PumsBirthplace.id), primary_key=True)
