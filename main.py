import yaml
from datetime import datetime
import time
import pytz
import tweepy

# import the astral library to get sunrise times
from astral.sun import sun
from astral.geocoder import database, lookup

# from tweet_parameters import placeholders


def get_next_sunrise(city: str):
    """Returns the next sunrise time for the specified city as a UTC datetime object."""
    # get a LocationInfo object for the specified city
    try:
        city = lookup(city, database())
    except KeyError:
        raise ValueError(
            f"City '{city}' not found in the database. For a list of valid cities, see https://sffjunkie.github.io/astral/#cities"
        )
    # get the next sunrise time for the specified city
    return sun(city.observer, date=date.today(), tzinfo=pytz.utc).get("sunrise")


def tweet(api, tweet_content):
    # tweet the message
    api.update_status(tweet_content)
    print(f"Tweeted: {tweet_content} at {datetime.now()}")


def convert_utc_to_local(utc_datetime: datetime):
    """Converts a UTC datetime object to a system local datetime object."""
    return utc_datetime.astimezone(pytz.timezone(time.tzname[0]))


def is_sunrise(city: str):
    """Returns True if it is currently sunrise in the specified city, otherwise returns False."""
    # get the next sunrise time for the specified city
    sun = get_next_sunrise(city)
    # get the local time for the next sunrise time for the specified city
    l_sun = convert_utc_to_local(sun)

    l_time = datetime.now()
    return l_sun.hour == l_time.hour and l_sun.minute == l_time.minute


def fill_tweet_placeholder(tweet_content: str, *values: str):
    """Replaces the placeholders in the tweet content with the specified values (if any)."""
    # if no values are passed, return the tweet content as is
    if len(values) == 0:
        return tweet_content
    # loop through the values and replace the placeholders with the values
    for i, value in enumerate(values):
        tweet_content = tweet_content.replace(f"{{{i+1}}}", str(value))
    return tweet_content


# ZmanimAPI Sectoin added as an extra to this file
from zmanim_api import *


def get_loc_with_zmanim() -> list[dict]:
    locations = [
        {"city": Cities.JERUSALEM, "zmanim": None},
        {"city": Cities.TEL_AVIV, "zmanim": None},
        {"city": Cities.HAIFA, "zmanim": None},
        {"city": Cities.BEER_SHEVA, "zmanim": None},
    ]

    for location in locations:
        zmanim = ZmanimAPI.get_zmanim(date=date.today(), city=location["city"])
        location["zmanim"] = zmanim[0].get_important_zmanim()

    return locations


def format_zmanim_for_tweet(zmanim: list[dict]) -> str:
    """Format the zmanim for the tweet
    zmanim (dict): a list of dicts with the keys "city" and "zmanim"
    """
    tweet = ""
    first_city_zmanim = zmanim[0]["zmanim"]
    zmanim_names = [zman.heb_title for zman in first_city_zmanim]
    for i, zmanim_name in enumerate(zmanim_names):
        tweet += f"{zmanim_name}:\n"
        for location in zmanim:
            tweet += (
                f"\t{location['city'].value.heb_name}: {location['zmanim'][i].time}\n"
            )
        tweet += "\n"

    return tweet


def main():
    # read the config data from the config.yaml file. this is a yaml file because it's easier to read and write than a json file
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # create an API client using the Twitter API keys and tokens from the config
    auth = tweepy.OAuthHandler(config["consumerKey"], config["consumerSecret"])
    auth.set_access_token(config["accessToken"], config["accessTokenSecret"])
    api = tweepy.API(auth)

    # after sunrise is reached, hold for 22 hours and start checking again
    while True:
        if is_sunrise(config["city"]):
            zmanim_str = format_zmanim_for_tweet(get_loc_with_zmanim())
            tweet(api, fill_tweet_placeholder(config["tweetContent"], zmanim_str))
            time.sleep(22 * 60 * 60)
        else:
            time.sleep(60)


if __name__ == "__main__":
    main()
