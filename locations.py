from pydantic import BaseModel, validator, Field, root_validator
from typing import Optional
from enum import Enum


class TimeZone(BaseModel):
    name: str
    utc_offset: str
    extended_name: str


class TimeZones(Enum):
    """Enum of all timezones in the Chabad API"""

    GMT_12: TimeZone = (
        TimeZone(
            name="Etc*GMT~12",
            utc_offset="-12:00",
            extended_name="International Date Line West",
        ),
    )
    GMT_11: TimeZone = (
        TimeZone(
            name="Etc*GMT~11",
            utc_offset="-11:00",
            extended_name="Coordinated Universal Time-11",
        ),
    )
    ADAK: TimeZone = (
        TimeZone(
            name="America*Adak", utc_offset="-10:00", extended_name="Aleutian Islands"
        ),
    )
    GMT_10: TimeZone = (
        TimeZone(name="Etc*GMT~10", utc_offset="-10:00", extended_name="Hawaii"),
    )
    MARQUESAS: TimeZone = (
        TimeZone(
            name="Pacific*Marquesas",
            utc_offset="-09:30",
            extended_name="Marquesas Islands",
        ),
    )
    ANCHORAGE: TimeZone = (
        TimeZone(name="America*Anchorage", utc_offset="-09:00", extended_name="Alaska"),
    )
    GMT_9: TimeZone = (
        TimeZone(
            name="Etc*GMT~9",
            utc_offset="-09:00",
            extended_name="Coordinated Universal Time-09",
        ),
    )
    LOS_ANGELES: TimeZone = (
        TimeZone(
            name="America*Los_Angeles",
            utc_offset="-08:00",
            extended_name="Pacific Time (US &amp; Canada)",
        ),
    )
    SANTA_ISABEL: TimeZone = (
        TimeZone(
            name="America*Santa_Isabel",
            utc_offset="-08:00",
            extended_name="Baja California",
        ),
    )
    GMT_8: TimeZone = (
        TimeZone(
            name="Etc*GMT~8",
            utc_offset="-08:00",
            extended_name="Coordinated Universal Time-08",
        ),
    )
    BOISE: TimeZone = (
        TimeZone(
            name="America*Boise",
            utc_offset="-07:00",
            extended_name="Mountain Time (US &amp; Canada)",
        ),
    )
    CHIHUAHUA: TimeZone = (
        TimeZone(
            name="America*Chihuahua",
            utc_offset="-07:00",
            extended_name="Chihuahua, La Paz, Mazatlan",
        ),
    )
    CRESTON: TimeZone = (
        TimeZone(name="America*Creston", utc_offset="-07:00", extended_name="Yukon"),
    )
    HERMOSILLO: TimeZone = (
        TimeZone(
            name="America*Hermosillo", utc_offset="-07:00", extended_name="Arizona"
        ),
    )
    BAHIA_BANDERAS: TimeZone = (
        TimeZone(
            name="America*Bahia_Banderas",
            utc_offset="-06:00",
            extended_name="Guadalajara, Mexico City, Monterrey",
        ),
    )
    BELIZE: TimeZone = (
        TimeZone(
            name="America*Belize", utc_offset="-06:00", extended_name="Central America"
        ),
    )
    CHICAGO: TimeZone = (
        TimeZone(
            name="America*Chicago",
            utc_offset="-06:00",
            extended_name="Central Time (US &amp; Canada)",
        ),
    )
    REGINA: TimeZone = (
        TimeZone(
            name="America*Regina", utc_offset="-06:00", extended_name="Saskatchewan"
        ),
    )
    EASTER: TimeZone = (
        TimeZone(
            name="Pacific*Easter", utc_offset="-06:00", extended_name="Easter Island"
        ),
    )
    BOGOTA: TimeZone = (
        TimeZone(
            name="America*Bogota",
            utc_offset="-05:00",
            extended_name="Bogota, Lima, Quito, Rio Branco",
        ),
    )
    CANCUN: TimeZone = (
        TimeZone(name="America*Cancun", utc_offset="-05:00", extended_name="Chetumal"),
    )
    DETROIT: TimeZone = (
        TimeZone(
            name="America*Detroit",
            utc_offset="-05:00",
            extended_name="Eastern Time (US &amp; Canada)",
        ),
    )
    GRAND_TURK: TimeZone = (
        TimeZone(
            name="America*Grand_Turk",
            utc_offset="-05:00",
            extended_name="Turks and Caicos",
        ),
    )
    HAVANA: TimeZone = (
        TimeZone(name="America*Havana", utc_offset="-05:00", extended_name="Havana"),
    )
    INDIANA_MARENGO: TimeZone = (
        TimeZone(
            name="America*Indiana*Marengo",
            utc_offset="-05:00",
            extended_name="Indiana (East)",
        ),
    )
    PORT_AU: TimeZone = (
        TimeZone(
            name="America*Port-au-Prince", utc_offset="-05:00", extended_name="Haiti"
        ),
    )
    ANGUILLA: TimeZone = (
        TimeZone(
            name="America*Anguilla",
            utc_offset="-04:00",
            extended_name="Georgetown, La Paz, Manaus, San Juan",
        ),
    )
    ASUNCION: TimeZone = (
        TimeZone(
            name="America*Asuncion", utc_offset="-04:00", extended_name="Asuncion"
        ),
    )
    CAMPO_GRANDE: TimeZone = (
        TimeZone(
            name="America*Campo_Grande", utc_offset="-04:00", extended_name="Cuiaba"
        ),
    )
    CARACAS: TimeZone = (
        TimeZone(name="America*Caracas", utc_offset="-04:00", extended_name="Caracas"),
    )
    GLACE_BAY: TimeZone = (
        TimeZone(
            name="America*Glace_Bay",
            utc_offset="-04:00",
            extended_name="Atlantic Time (Canada)",
        ),
    )
    SANTIAGO: TimeZone = (
        TimeZone(
            name="America*Santiago", utc_offset="-04:00", extended_name="Santiago"
        ),
    )
    ST_JOHNS: TimeZone = (
        TimeZone(
            name="America*St_Johns", utc_offset="-03:30", extended_name="Newfoundland"
        ),
    )
    ARAGUAINA: TimeZone = (
        TimeZone(
            name="America*Araguaina", utc_offset="-03:00", extended_name="Araguaina"
        ),
    )
    ARGENTINA_LA_RIOJA: TimeZone = (
        TimeZone(
            name="America*Argentina*La_Rioja",
            utc_offset="-03:00",
            extended_name="City of Buenos Aires",
        ),
    )
    BAHIA: TimeZone = (
        TimeZone(name="America*Bahia", utc_offset="-03:00", extended_name="Salvador"),
    )
    BELEM: TimeZone = (
        TimeZone(
            name="America*Belem",
            utc_offset="-03:00",
            extended_name="Cayenne, Fortaleza",
        ),
    )
    GODTHAB: TimeZone = (
        TimeZone(
            name="America*Godthab", utc_offset="-03:00", extended_name="Greenland"
        ),
    )
    MIQUELON: TimeZone = (
        TimeZone(
            name="America*Miquelon",
            utc_offset="-03:00",
            extended_name="Saint Pierre and Miquelon",
        ),
    )
    MONTEVIDEO: TimeZone = (
        TimeZone(
            name="America*Montevideo", utc_offset="-03:00", extended_name="Montevideo"
        ),
    )
    PUNTA_ARENAS: TimeZone = (
        TimeZone(
            name="America*Punta_Arenas",
            utc_offset="-03:00",
            extended_name="Punta Arenas",
        ),
    )
    SAO_PAULO: TimeZone = (
        TimeZone(
            name="America*Sao_Paulo", utc_offset="-03:00", extended_name="Brasilia"
        ),
    )
    NORONHA: TimeZone = (
        TimeZone(
            name="America*Noronha",
            utc_offset="-02:00",
            extended_name="Coordinated Universal Time-02",
        ),
    )
    SCORESBYSUND: TimeZone = (
        TimeZone(
            name="America*Scoresbysund", utc_offset="-01:00", extended_name="Azores"
        ),
    )
    CAPE_VERDE: TimeZone = (
        TimeZone(
            name="Atlantic*Cape_Verde",
            utc_offset="-01:00",
            extended_name="Cabo Verde Is.",
        ),
    )
    ABIDJAN: TimeZone = (
        TimeZone(
            name="Africa*Abidjan",
            utc_offset="+00:00",
            extended_name="Monrovia, Reykjavik",
        ),
    )
    SAO_TOME: TimeZone = (
        TimeZone(name="Africa*Sao_Tome", utc_offset="+00:00", extended_name="Sao Tome"),
    )
    DANMARKSHAVN: TimeZone = (
        TimeZone(
            name="America*Danmarkshavn",
            utc_offset="+00:00",
            extended_name="Coordinated Universal Time",
        ),
    )
    CANARY: TimeZone = (
        TimeZone(
            name="Atlantic*Canary",
            utc_offset="+00:00",
            extended_name="Dublin, Edinburgh, Lisbon, London",
        ),
    )
    ALGIERS: TimeZone = (
        TimeZone(
            name="Africa*Algiers",
            utc_offset="+01:00",
            extended_name="West Central Africa",
        ),
    )
    CASABLANCA: TimeZone = (
        TimeZone(
            name="Africa*Casablanca", utc_offset="+01:00", extended_name="Casablanca"
        ),
    )
    CEUTA: TimeZone = (
        TimeZone(
            name="Africa*Ceuta",
            utc_offset="+01:00",
            extended_name="Brussels, Copenhagen, Madrid, Paris",
        ),
    )
    LONGYEARBYEN: TimeZone = (
        TimeZone(
            name="Arctic*Longyearbyen",
            utc_offset="+01:00",
            extended_name="Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna",
        ),
    )
    BELGRADE: TimeZone = (
        TimeZone(
            name="Europe*Belgrade",
            utc_offset="+01:00",
            extended_name="Belgrade, Bratislava, Budapest, Ljubljana, Prague",
        ),
    )
    SARAJEVO: TimeZone = (
        TimeZone(
            name="Europe*Sarajevo",
            utc_offset="+01:00",
            extended_name="Sarajevo, Skopje, Warsaw, Zagreb",
        ),
    )
    BLANTYRE: TimeZone = (
        TimeZone(
            name="Africa*Blantyre",
            utc_offset="+02:00",
            extended_name="Harare, Pretoria",
        ),
    )
    CAIRO: TimeZone = (
        TimeZone(name="Africa*Cairo", utc_offset="+02:00", extended_name="Cairo"),
    )
    KHARTOUM: TimeZone = (
        TimeZone(name="Africa*Khartoum", utc_offset="+02:00", extended_name="Khartoum"),
    )
    TRIPOLI: TimeZone = (
        TimeZone(name="Africa*Tripoli", utc_offset="+02:00", extended_name="Tripoli"),
    )
    WINDHOEK: TimeZone = (
        TimeZone(name="Africa*Windhoek", utc_offset="+02:00", extended_name="Windhoek"),
    )
    AMMAN: TimeZone = (
        TimeZone(name="Asia*Amman", utc_offset="+02:00", extended_name="Amman"),
    )
    BEIRUT: TimeZone = (
        TimeZone(name="Asia*Beirut", utc_offset="+02:00", extended_name="Beirut"),
    )
    DAMASCUS: TimeZone = (
        TimeZone(name="Asia*Damascus", utc_offset="+02:00", extended_name="Damascus"),
    )
    FAMAGUSTA: TimeZone = (
        TimeZone(
            name="Asia*Famagusta",
            utc_offset="+02:00",
            extended_name="Athens, Bucharest",
        ),
    )
    GAZA: TimeZone = (
        TimeZone(name="Asia*Gaza", utc_offset="+02:00", extended_name="Gaza, Hebron"),
    )
    JERUSALEM: TimeZone = (
        TimeZone(name="Asia*Jerusalem", utc_offset="+02:00", extended_name="Jerusalem"),
    )
    CHISINAU: TimeZone = (
        TimeZone(name="Europe*Chisinau", utc_offset="+02:00", extended_name="Chisinau"),
    )
    HELSINKI: TimeZone = (
        TimeZone(
            name="Europe*Helsinki",
            utc_offset="+02:00",
            extended_name="Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius",
        ),
    )
    KALININGRAD: TimeZone = (
        TimeZone(
            name="Europe*Kaliningrad", utc_offset="+02:00", extended_name="Kaliningrad"
        ),
    )
    ADDIS_ABABA: TimeZone = (
        TimeZone(
            name="Africa*Addis_Ababa", utc_offset="+03:00", extended_name="Nairobi"
        ),
    )
    ADEN: TimeZone = (
        TimeZone(name="Asia*Aden", utc_offset="+03:00", extended_name="Kuwait, Riyadh"),
    )
    BAGHDAD: TimeZone = (
        TimeZone(name="Asia*Baghdad", utc_offset="+03:00", extended_name="Baghdad"),
    )
    ISTANBUL: TimeZone = (
        TimeZone(name="Europe*Istanbul", utc_offset="+03:00", extended_name="Istanbul"),
    )
    KIROV: TimeZone = (
        TimeZone(
            name="Europe*Kirov",
            utc_offset="+03:00",
            extended_name="Moscow, St. Petersburg",
        ),
    )
    MINSK: TimeZone = (
        TimeZone(name="Europe*Minsk", utc_offset="+03:00", extended_name="Minsk"),
    )
    VOLGOGRAD: TimeZone = (
        TimeZone(
            name="Europe*Volgograd", utc_offset="+03:00", extended_name="Volgograd"
        ),
    )
    TEHRAN: TimeZone = (
        TimeZone(name="Asia*Tehran", utc_offset="+03:30", extended_name="Tehran"),
    )
    BAKU: TimeZone = (
        TimeZone(name="Asia*Baku", utc_offset="+04:00", extended_name="Baku"),
    )
    DUBAI: TimeZone = (
        TimeZone(
            name="Asia*Dubai", utc_offset="+04:00", extended_name="Abu Dhabi, Muscat"
        ),
    )
    TBILISI: TimeZone = (
        TimeZone(name="Asia*Tbilisi", utc_offset="+04:00", extended_name="Tbilisi"),
    )
    YEREVAN: TimeZone = (
        TimeZone(name="Asia*Yerevan", utc_offset="+04:00", extended_name="Yerevan"),
    )
    ASTRAKHAN: TimeZone = (
        TimeZone(
            name="Europe*Astrakhan",
            utc_offset="+04:00",
            extended_name="Astrakhan, Ulyanovsk",
        ),
    )
    SAMARA: TimeZone = (
        TimeZone(
            name="Europe*Samara", utc_offset="+04:00", extended_name="Izhevsk, Samara"
        ),
    )
    SARATOV: TimeZone = (
        TimeZone(name="Europe*Saratov", utc_offset="+04:00", extended_name="Saratov"),
    )
    MAHE: TimeZone = (
        TimeZone(name="Indian*Mahe", utc_offset="+04:00", extended_name="Port Louis"),
    )
    KABUL: TimeZone = (
        TimeZone(name="Asia*Kabul", utc_offset="+04:30", extended_name="Kabul"),
    )
    MAWSON: TimeZone = (
        TimeZone(
            name="Antarctica*Mawson",
            utc_offset="+05:00",
            extended_name="Ashgabat, Tashkent",
        ),
    )
    KARACHI: TimeZone = (
        TimeZone(
            name="Asia*Karachi", utc_offset="+05:00", extended_name="Islamabad, Karachi"
        ),
    )
    QYZYLORDA: TimeZone = (
        TimeZone(name="Asia*Qyzylorda", utc_offset="+05:00", extended_name="Qyzylorda"),
    )
    YEKATERINBURG: TimeZone = (
        TimeZone(
            name="Asia*Yekaterinburg", utc_offset="+05:00", extended_name="Ekaterinburg"
        ),
    )
    CALCUTTA: TimeZone = (
        TimeZone(
            name="Asia*Calcutta",
            utc_offset="+05:30",
            extended_name="Chennai, Kolkata, Mumbai, New Delhi",
        ),
    )
    COLOMBO: TimeZone = (
        TimeZone(
            name="Asia*Colombo",
            utc_offset="+05:30",
            extended_name="Sri Jayawardenepura",
        ),
    )
    KATMANDU: TimeZone = (
        TimeZone(name="Asia*Katmandu", utc_offset="+05:45", extended_name="Kathmandu"),
    )
    VOSTOK: TimeZone = (
        TimeZone(name="Antarctica*Vostok", utc_offset="+06:00", extended_name="Astana"),
    )
    DHAKA: TimeZone = (
        TimeZone(name="Asia*Dhaka", utc_offset="+06:00", extended_name="Dhaka"),
    )
    OMSK: TimeZone = (
        TimeZone(name="Asia*Omsk", utc_offset="+06:00", extended_name="Omsk"),
    )
    RANGOON: TimeZone = (
        TimeZone(
            name="Asia*Rangoon", utc_offset="+06:30", extended_name="Yangon (Rangoon)"
        ),
    )
    DAVIS: TimeZone = (
        TimeZone(
            name="Antarctica*Davis",
            utc_offset="+07:00",
            extended_name="Bangkok, Hanoi, Jakarta",
        ),
    )
    BARNAUL: TimeZone = (
        TimeZone(
            name="Asia*Barnaul",
            utc_offset="+07:00",
            extended_name="Barnaul, Gorno-Altaysk",
        ),
    )
    HOVD: TimeZone = (
        TimeZone(name="Asia*Hovd", utc_offset="+07:00", extended_name="Hovd"),
    )
    KRASNOYARSK: TimeZone = (
        TimeZone(
            name="Asia*Krasnoyarsk", utc_offset="+07:00", extended_name="Krasnoyarsk"
        ),
    )
    NOVOSIBIRSK: TimeZone = (
        TimeZone(
            name="Asia*Novosibirsk", utc_offset="+07:00", extended_name="Novosibirsk"
        ),
    )
    TOMSK: TimeZone = (
        TimeZone(name="Asia*Tomsk", utc_offset="+07:00", extended_name="Tomsk"),
    )
    BRUNEI: TimeZone = (
        TimeZone(
            name="Asia*Brunei",
            utc_offset="+08:00",
            extended_name="Kuala Lumpur, Singapore",
        ),
    )
    CHOIBALSAN: TimeZone = (
        TimeZone(
            name="Asia*Choibalsan", utc_offset="+08:00", extended_name="Ulaanbaatar"
        ),
    )
    HONG_KONG: TimeZone = (
        TimeZone(
            name="Asia*Hong_Kong",
            utc_offset="+08:00",
            extended_name="Beijing, Chongqing, Hong Kong, Urumqi",
        ),
    )
    IRKUTSK: TimeZone = (
        TimeZone(name="Asia*Irkutsk", utc_offset="+08:00", extended_name="Irkutsk"),
    )
    TAIPEI: TimeZone = (
        TimeZone(name="Asia*Taipei", utc_offset="+08:00", extended_name="Taipei"),
    )
    PERTH: TimeZone = (
        TimeZone(name="Australia*Perth", utc_offset="+08:00", extended_name="Perth"),
    )
    EUCLA: TimeZone = (
        TimeZone(name="Australia*Eucla", utc_offset="+08:45", extended_name="Eucla"),
    )
    CHITA: TimeZone = (
        TimeZone(name="Asia*Chita", utc_offset="+09:00", extended_name="Chita"),
    )
    DILI: TimeZone = (
        TimeZone(
            name="Asia*Dili", utc_offset="+09:00", extended_name="Osaka, Sapporo, Tokyo"
        ),
    )
    KHANDYGA: TimeZone = (
        TimeZone(name="Asia*Khandyga", utc_offset="+09:00", extended_name="Yakutsk"),
    )
    PYONGYANG: TimeZone = (
        TimeZone(name="Asia*Pyongyang", utc_offset="+09:00", extended_name="Pyongyang"),
    )
    SEOUL: TimeZone = (
        TimeZone(name="Asia*Seoul", utc_offset="+09:00", extended_name="Seoul"),
    )
    ADELAIDE: TimeZone = (
        TimeZone(
            name="Australia*Adelaide", utc_offset="+09:30", extended_name="Adelaide"
        ),
    )
    DARWIN: TimeZone = (
        TimeZone(name="Australia*Darwin", utc_offset="+09:30", extended_name="Darwin"),
    )
    DUMONTDURVILLE: TimeZone = (
        TimeZone(
            name="Antarctica*DumontDUrville",
            utc_offset="+10:00",
            extended_name="Guam, Port Moresby",
        ),
    )
    MACQUARIE: TimeZone = (
        TimeZone(
            name="Antarctica*Macquarie", utc_offset="+10:00", extended_name="Hobart"
        ),
    )
    UST_NERA: TimeZone = (
        TimeZone(
            name="Asia*Ust-Nera", utc_offset="+10:00", extended_name="Vladivostok"
        ),
    )
    BRISBANE: TimeZone = (
        TimeZone(
            name="Australia*Brisbane", utc_offset="+10:00", extended_name="Brisbane"
        ),
    )
    MELBOURNE: TimeZone = (
        TimeZone(
            name="Australia*Melbourne",
            utc_offset="+10:00",
            extended_name="Canberra, Melbourne, Sydney",
        ),
    )
    LORD_HOWE: TimeZone = (
        TimeZone(
            name="Australia*Lord_Howe",
            utc_offset="+10:30",
            extended_name="Lord Howe Island",
        ),
    )
    CASEY: TimeZone = (
        TimeZone(
            name="Antarctica*Casey",
            utc_offset="+11:00",
            extended_name="Solomon Is., New Caledonia",
        ),
    )
    MAGADAN: TimeZone = (
        TimeZone(name="Asia*Magadan", utc_offset="+11:00", extended_name="Magadan"),
    )
    SAKHALIN: TimeZone = (
        TimeZone(name="Asia*Sakhalin", utc_offset="+11:00", extended_name="Sakhalin"),
    )
    SREDNEKOLYMSK: TimeZone = (
        TimeZone(
            name="Asia*Srednekolymsk", utc_offset="+11:00", extended_name="Chokurdakh"
        ),
    )
    BOUGAINVILLE: TimeZone = (
        TimeZone(
            name="Pacific*Bougainville",
            utc_offset="+11:00",
            extended_name="Bougainville Island",
        ),
    )
    NORFOLK: TimeZone = (
        TimeZone(
            name="Pacific*Norfolk", utc_offset="+11:00", extended_name="Norfolk Island"
        ),
    )
    MCMURDO: TimeZone = (
        TimeZone(
            name="Antarctica*McMurdo",
            utc_offset="+12:00",
            extended_name="Auckland, Wellington",
        ),
    )
    ANADYR: TimeZone = (
        TimeZone(
            name="Asia*Anadyr",
            utc_offset="+12:00",
            extended_name="Anadyr, Petropavlovsk-Kamchatsky",
        ),
    )
    GMT_PLUS_12: TimeZone = (
        TimeZone(
            name="Etc*GMT-12",
            utc_offset="+12:00",
            extended_name="Coordinated Universal Time+12",
        ),
    )
    FIJI: TimeZone = (
        TimeZone(name="Pacific*Fiji", utc_offset="+12:00", extended_name="Fiji"),
    )
    CHATHAM: TimeZone = (
        TimeZone(
            name="Pacific*Chatham", utc_offset="+12:45", extended_name="Chatham Islands"
        ),
    )
    GMT_13: TimeZone = (
        TimeZone(
            name="Etc*GMT-13",
            utc_offset="+13:00",
            extended_name="Coordinated Universal Time+13",
        ),
    )
    APIA: TimeZone = (
        TimeZone(name="Pacific*Apia", utc_offset="+13:00", extended_name="Samoa"),
    )
    TONGATAPU: TimeZone = (
        TimeZone(
            name="Pacific*Tongatapu", utc_offset="+13:00", extended_name="Nuku'alofa"
        ),
    )
    GMT_14: TimeZone = TimeZone(
        name="Etc*GMT-14", utc_offset="+14:00", extended_name="Kiritimati Island"
    )

    # this will eliminate the need to use .value[0] to get the city info
    def __init__(self, time_zone: TimeZone):
        self._value_ = time_zone


class LocationType(Enum):
    CITY = 1
    ZIP_CODE = 2
    COORDINATES = 3


class Coordinates(BaseModel):
    lat: float
    lon: float
    time_zone: TimeZone
    custom_name: Optional[str] = "Default location name"
    http_format: Optional[str] = None

    # read only field
    type: LocationType = Field(LocationType.COORDINATES, const=True)

    @validator("http_format")
    def http_format_validator(cls, v):
        if v:
            raise ValueError("http_format is read only")

        return f"{cls.lat},{cls.lon}"


class CityInfo(BaseModel):
    heb_name: str
    eng_name: str
    location_id: int
    astral_city_name: Optional[str] = None

    # read only field
    type: LocationType = Field(LocationType.CITY, const=True)


class Location(BaseModel):
    city: Optional[CityInfo] = None
    coordinates: Optional[Coordinates] = None

    # read only field
    type: Optional[LocationType] = None

    @root_validator
    def type_validator(cls, values):
        # if type is provided, raise an error
        if values.get("type"):
            raise ValueError("type is read only")

        # duplicate or no location was provided
        if values.get("city") and values.get("coordinates"):
            raise ValueError("Only one type of location is allowed")

        if values.get("city") is None and values.get("coordinates") is None:
            raise ValueError("No/invalid location was provided")

        # set the type of location
        if values.get("city"):
            values["type"] = LocationType.CITY
        if values.get("coordinates"):
            values["type"] = LocationType.COORDINATES

        return values


class Cities(Enum):
    """Enum of of popular cities. I will happaly add more cities if you ask.
    To get the id of a city you have to got to chabad.org and check the network tab when you search for a city.
    """

    JERUSALEM: CityInfo = (
        CityInfo(
            heb_name="ירושלים", eng_name="Jerusalem", location_id=247, location_type=1
        ),
    )
    TEL_AVIV: CityInfo = (
        CityInfo(
            heb_name="תל אביב", eng_name="Tel Aviv", location_id=531, location_type=1
        ),
    )
    HAIFA: CityInfo = (
        CityInfo(heb_name="חיפה", eng_name="Haifa", location_id=689, location_type=1),
    )
    BEER_SHEVA: CityInfo = (
        CityInfo(
            heb_name="באר שבע", eng_name="Beer Sheva", location_id=688, location_type=1
        ),
    )

    # this will eliminate the need to use .value[0] to get the city info
    def __init__(self, city_info: CityInfo):
        self._value_ = city_info
