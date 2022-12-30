import requests
from typing import Optional
from pydantic import BaseModel, Field, root_validator
from locations import *
from datetime import date, timedelta


class ZmanimRequest(BaseModel):
    date: Optional[date]
    start_date: Optional[date]
    end_date: Optional[date]
    location: Location
    language: str = Field("he", regex="^(he|en)$")

    @root_validator
    def date_validator(cls, values):
        # 1. if date is given then start_date and end_date are not allowed
        if values.get("date") and (values.get("start_date") or values.get("end_date")):
            raise ValueError(
                "For a single date, use date instead of start_date and end_date, they are not allowed together"
            )

        if values.get("date"):
            values["date"] = values["date"].strftime("%m/%d/%Y")
            return values

        if values.get("start_date") == values.get("end_date"):
            raise ValueError("End date must ne at least one day after start date")

        if values.get("start_date") > values.get("end_date"):
            raise ValueError("start_date must be before end_date")

        if values.get("end_date") - values.get("start_date") > timedelta(days=180):
            raise ValueError("The maximum range is 180 days")

        values["start_date"] = values["start_date"].strftime("%m/%d/%Y")
        values["end_date"] = values["end_date"].strftime("%m/%d/%Y")
        return values


class ChabadAPI:
    BASE_URL = "chabad.org/webservices/zmanim/zmanim/Get_Zmanim"
    HEADERS = dict(
        accept="application/json",
    )

    def __init__(self):
        pass

    def get_zmanim(self, r: ZmanimRequest) -> dict:
        """Get the zmanim for the given location and date
        Can be used to get zmanim for a single day or a range of days (up to 6 months)

        Example:
            # Get zmanim for a range of dates, location via city
            >>> request = ZmanimRequest(
                start_date=date(2021, 1, 3),
                end_date=date(2021, 10, 1),
                location=Location(city=Cities.TEL_AVIV.value)
            )
            >>> zmanim = ChabadAPI().get_zmanim(request)

            # Get zmanim for a single date, location via coordinates
            >>> request = ZmanimRequest(
                    start_date=date(2021, 1, 3),
                    end_date=date(2021, 2, 1),
                    location=Location(coordinates=Coordinates(lat=32.08088, lon=34.78057, custom_name="Tel Aviv", time_zone=TimeZones.JERUSALEM.value))
                )

                zmanim = ChabadAPI().get_zmanim(request)

            # Of course, you can mix and match the two
            # Maybe some day Ill add an option to get via us zip code

        Args:
            r (ZmanimRequest): The request object containing the location and date information
        """

        url = f"https://www.{r.language + '.' if r.language != 'en' else ''}{self.BASE_URL}"

        # Create the parameters for the request
        params = {
            "locationtype": r.location.type,
            "tdate": r.date,
            "startdate": r.start_date,
            "enddate": r.end_date,
        }

        if r.location.type == LocationType.CITY:
            params["locationid"] = r.location.city.location_id

        coords_params = {}
        if r.location.type == LocationType.COORDINATES:
            params["coords"] = r.location.coordinates.http_format
            params["n"] = r.location.coordinates.custom_name
            params["tzname"] = r.location.coordinates.time_zone.name

        response = requests.get(url, params=params, headers=self.HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch zmanim")
