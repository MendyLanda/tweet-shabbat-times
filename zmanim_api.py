from pydantic import BaseModel, Field
from chabad_org_wrapper import (
    ChabadAPI,
    ZmanimRequest,
    Cities,
    Location,
    Coordinates,
    LocationType,
    TimeZones,
)
from locations import CityInfo
from datetime import date, datetime, timedelta
from typing import Optional
from copy import deepcopy


class Zman(BaseModel):
    name: str  # Needs to be english
    eng_title: str
    heb_title: str
    time: Optional[str] = None
    raw_title: Optional[str] = None
    foot_note_type: Optional[str] = None


class Day(BaseModel):
    date: date
    day_of_week: int = Field(max=6, min=0)
    is_holiday: bool
    is_fast_day: Optional[bool] = None
    holiday_name: Optional[str] = None
    parsha: Optional[str] = None


class LocationInfo(BaseModel):
    name: str


class ZmanimTypes:
    AlosHashachar = Zman(
        name="AlosHashachar", heb_title="עלות השחר", eng_title="Alos Hashachar"
    )
    EarliestTefillin = Zman(
        name="EarliestTefillin", heb_title="משיכיר", eng_title="Earliest Tefillin"
    )
    NetzHachamah = Zman(
        name="NetzHachamah", heb_title="נץ החמה", eng_title="Netz Hachamah"
    )
    LatestShema = Zman(
        name="LatestShema", heb_title="סוף זמן קריאת שמע", eng_title="Latest Shema"
    )
    LatestTefillah = Zman(
        name="LatestTefillah", heb_title="סוף זמן תפילה", eng_title="Latest Tefillah"
    )
    Chatzos = Zman(name="Chatzos", heb_title="חצות (היום)", eng_title="Chatzos")
    MinchahGedolah = Zman(
        name="MinchahGedolah", heb_title="מנחה גדולה", eng_title="Minchah Gedolah"
    )
    MinchahKetanah = Zman(
        name="MinchahKetanah", heb_title="מנחה קטנה", eng_title="Minchah Ketanah"
    )
    PlagHaminchah = Zman(
        name="PlagHaminchah", heb_title="פלג המנחה", eng_title="Plag Haminchah"
    )
    Shkiah = Zman(name="Shkiah", heb_title="שקיעה", eng_title="Shkiah")
    CandleLighting = Zman(
        name="CandleLighting", heb_title="הדלקת נרות", eng_title="Candle Lighting"
    )
    ShabbatEndTime = Zman(
        name="ShabbatEndTime", heb_title="צאת שבת", eng_title="Shabbat End Time"
    )
    ChatzosNight = Zman(
        name="ChatzosNight", heb_title="חצות (הלילה)", eng_title="Chatzos Night"
    )
    ShaahZmanit = Zman(
        name="ShaahZmanit", heb_title="שעה זמנית", eng_title="Shaah Zmanit"
    )
    Tzeis = Zman(name="Tzeis", heb_title="צאת הכוכבים", eng_title="Tzeis")
    FastEnds = Zman(name="FastEnds", heb_title="צאת הצום", eng_title="Fast Ends")
    FastStarts = Zman(
        name="FastStarts", heb_title="התחלת הצום", eng_title="Fast Starts"
    )
    LastEatingChametzTime = Zman(
        name="LastEatingChametzTime",
        heb_title="סוף זמן אכילת חמץ",
        eng_title="Last Eating Chametz Time",
    )
    BurnChametzTime = Zman(
        name="BurnChametzTime", heb_title="ביעור חמץ", eng_title="Burn Chametz Time"
    )
    BedikatChametz = Zman(
        name="BedikatChametz", heb_title="בדיקת חמץ", eng_title="Bedikat Chametz"
    )
    SecondDayCandleLighting = Zman(
        name="SecondDayCandleLighting",
        heb_title="הדלקת נרות יום שני",
        eng_title="Second Day Candle Lighting",
    )
    ThirdDayCandleLighting = Zman(
        name="ThirdDayCandleLighting",
        heb_title="הדלקת נרות יום שלישי",
        eng_title="Third Day Candle Lighting",
    )

    @classmethod
    def get_zman(cls, name: str) -> Zman:
        return deepcopy(getattr(cls, name))


class ZmanimDay:
    """Zmanim class contains all the zmanim for a given day"""

    def __init__(self, day: Day):
        self.day = day
        self.zmanim: dict[Zman] = {}

    def add_zman(self, zman: Zman) -> None:
        if zman.name not in self.zmanim:
            self.zmanim[zman.name] = zman
        else:
            raise ValueError(f"Zman {zman.name} already exists")

    def add_location_data(self, location: Location) -> None:
        # TODO: add more details to location info, enable english names
        if location.type == LocationType.CITY:
            self.location = LocationInfo(name=location.city.heb_name)
        elif location.type == LocationType.COORDINATES:
            self.location = LocationInfo(name=location.coordinates.custom_name)

    def is_fast_day(self) -> bool:
        return (
            ZmanimTypes.FastEnds.name in self.zmanim
            or ZmanimTypes.FastStarts.name in self.zmanim
        )

    def is_shabbat(self) -> bool:
        return (
            ZmanimTypes.ShabbatEndTime.name in self.zmanim and not self.day.is_holiday
        )

    def is_erev_shabbat(self) -> bool:
        """Check if the day is erev shabbat or yom tov"""
        return ZmanimTypes.CandleLighting.name in self.zmanim

    def is_second_e_shabbat(self) -> bool:
        """Check if the day is shabbat after a holiday or second youm tov
        For example, if the day is a holiday and the next day is shabbat, then the next day is a second shabbat

        Returns:
            bool: True if the day is a second shabbat, False otherwise
        """
        # check if ShabbatEndTime is in the zmanim and if the foot_note_type is of type "LightCandlesAfter"
        if ZmanimTypes.ShabbatEndTime.name in self.zmanim:
            return (
                self.zmanim[ZmanimTypes.ShabbatEndTime.name].foot_note_type
                == "LightCandlesAfter"
            )

        # if the day is friday and there is a candle lighting or more already, then it is a second shabbat
        if self.day.day_of_week == 5:
            return (
                ZmanimTypes.CandleLighting.name in self.zmanim
                or ZmanimTypes.SecondDayCandleLighting.name in self.zmanim
            )

        return False

    def avilable_zmanim(self) -> list[str]:
        return self.zmanim.keys()

    def get_zman(self, zman: ZmanimTypes) -> Optional[Zman]:
        if zman.name in self.zmanim:
            return self.zmanim[zman.name]
        else:
            raise KeyError(
                f"Zman {zman.name} is not available for this day. Available zmanim are: {self.avilable_zmanim()}"
            )

    def get_zman_by_name(self, zman_name: str) -> Zman:
        return self.zmanim[zman_name]

    def get_zman_by_heb_title(self, heb_title: str) -> Zman:
        for zman in self.zmanim:
            if zman.heb_title == heb_title:
                return zman
        return None

    def get_important_zmanim(self) -> list[Zman]:
        """Get a list of the important zmanim for the day

        Important zmanim are:
        - Fast Starts
        - Fast Ends
        - Bedikat Chametz
        - Last Eating Chametz Time
        - Burn Chametz Time
        - Candle Lighting
        - Second Day Candle Lighting
        - Third Day Candle Lighting
        - Shabbat End Time

        Returns:
            list[Zman]: Populated list of important zmanim
        """
        important_zmanim = []
        for zman in self.zmanim:
            if zman in [
                ZmanimTypes.FastStarts.name,
                ZmanimTypes.FastEnds.name,
                ZmanimTypes.BedikatChametz.name,
                ZmanimTypes.LastEatingChametzTime.name,
                ZmanimTypes.BurnChametzTime.name,
                ZmanimTypes.CandleLighting.name,
                ZmanimTypes.SecondDayCandleLighting.name,
                ZmanimTypes.ThirdDayCandleLighting.name,
                ZmanimTypes.ShabbatEndTime.name,
            ]:
                important_zmanim.append(self.get_zman_by_name(zman))
        return important_zmanim


class ZmanimAPI:
    def __init__(self, city: CityInfo, date: date):
        self.get_zmanim(city, date)

    @staticmethod
    def format_response(response: dict) -> ZmanimDay:
        resp_zmanim = response["Days"][0]["TimeGroups"]

        day = Day(
            date=datetime.strptime(response["Days"][0]["DisplayDate"], "%m/%d/%Y"),
            day_of_week=response["Days"][0]["DayOfWeek"],
            is_holiday=response["Days"][0]["IsHoliday"],
            holiday_name=response["Days"][0]["HolidayName"],
            parsha=response["Days"][0]["Parsha"],
        )

        zmanim = ZmanimDay(day)

        for zman in resp_zmanim:
            zman_type = ZmanimTypes.get_zman(zman["ZmanType"])
            zman_type.time = zman["Items"][0]["Zman"]
            zman_type.raw_title = zman["Title"]
            zman_type.foot_note_type = zman[
                "FootnoteType"
            ]  # used to check for successesive holidays
            zmanim.add_zman(zman_type)

        zmanim.day.is_fast_day = zmanim.is_fast_day()

        return zmanim

    @staticmethod
    def enrich_with_special_times(zmanim_days: list[ZmanimDay]) -> list[ZmanimDay]:
        """Enrich the zmanim with special times, like candle lighting and shabbat end time
        It is assumes the first day in zmanim_days is erev shabbat or yom tov

        Args:
            zmanim_days (list[ZmanimDay]): The zmanim to enrich

        Returns:
            ZmanimDay: The enriched zmanim
        """
        # loop through the next 3 days to find the next day that is not a second shabbat
        for i in range(1, 4):

            # for regular erev shabbat, the next day is shabbat
            if not zmanim_days[i].is_second_e_shabbat():
                zmanim_days[0].add_zman(
                    zmanim_days[i].get_zman(ZmanimTypes.ShabbatEndTime)
                )
                return zmanim_days

            # add the candle lighting time to the appropriate zmanim type
            if i == 1:
                extra_candle_lighting = ZmanimTypes.SecondDayCandleLighting
            elif i == 2:
                extra_candle_lighting = ZmanimTypes.ThirdDayCandleLighting
            # a third day is not possible here

            if ZmanimTypes.ShabbatEndTime.name not in zmanim_days[i].zmanim:
                extra_candle_lighting.time = (
                    zmanim_days[i].get_zman(ZmanimTypes.CandleLighting).time
                )  # If shabbat is in the middle or after a holiday, "Candle Lighting" is used.
            else:
                extra_candle_lighting.time = (
                    zmanim_days[i].get_zman(ZmanimTypes.ShabbatEndTime).time
                )  # "Shabbat Ends" is the same as "Candle Lighting" for second_e_shabbat

            zmanim_days[0].add_zman(extra_candle_lighting)

        return zmanim_days

    @staticmethod
    def call_chabad_api(request: ZmanimRequest) -> dict:
        return ChabadAPI().get_zmanim(request)

    @classmethod
    def get_zmanim(
        cls,
        date: date,
        days: int = 1,
        city: Optional[Cities] = None,
        coordinates: Optional[Coordinates] = None,
    ) -> list[ZmanimDay]:
        """Get zmanim for a given city and date from Chabad.org API
        The way this set up, every call will get the zmanim for a week from the given date, to acces

        For a list of zmanim types, see the ZmanimTypes enum in the zmanim_types module.

        Args:
            date (date): The date to get zmanim for
            days (int, optional): The number of days to get zmanim for. Defaults to 1, Max is 180.
            city (Optional[Cities], optional): The city to get zmanim for. Defaults to None. If city is provided, coordinates will be ignored.
            coordinates (Optional[Coordinates], optional): The coordinates to get zmanim for. Defaults to None.

        Examples:

            1. Get zmanim for Tel Aviv for 3 days using city location data
            response = ZmanimAPI.get_zmanim(date(2021, 9, 17), city=Cities.TEL_AVIV, days=3)

            2. Get zmanim for Tel Aviv for 1 day using coordinates
            response = ZmanimAPI.get_zmanim(
                date(2021, 9, 17),
                coordinates=Coordinates(
                    lat=32.0853,
                    lon=34.7818,
                    time_zone=TimeZones.JERUSALEM.value,
                    custom_name="Tel Aviv",
                ),
            )

        Returns:
            ZmanimDay: A list of ZmanimDay object containing all the zmanim for the day. sorted by date.
        """

        # validate input
        if city is None and coordinates is None:
            raise ValueError("Must provide either a city or coordinates")

        if days < 1 or days >= 180:
            raise ValueError("Days must be between 1 and 180")

        # set location
        if city is not None:
            location = Location(city=city.value)
        else:
            location = Location(coordinates=coordinates)

        # set dates
        start_date = date
        end_date = date + timedelta(
            days=4 if days < 4 else days
        )  # the minimum number of days we want is 4, because we need to check the next 3 days to get shabbat end times

        request = ZmanimRequest(
            location=location, start_date=start_date, end_date=end_date
        )

        response = cls.call_chabad_api(request)
        zmanim_days: list[ZmanimDay] = []

        for i in response["Days"]:
            zmanim_days.append(cls.format_response({"Days": [i]}))

        if zmanim_days[0].is_erev_shabbat():
            zmanim_days = cls.enrich_with_special_times(zmanim_days)

        # add location data to each day
        for day in zmanim_days:
            day.add_location_data(location)

        # return only the requested number of days
        return zmanim_days[:days]
