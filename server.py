import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/s.mahmoud97/api/concerts-artists-events-tracker'

mcp = FastMCP('concerts-artists-events-tracker')

@mcp.tool()
def search(keyword: Annotated[Union[str, None], Field(description='Search term to filter results by artist, event, festival, or venue name. For example, use Coldplay to find events related to the artist Coldplay')] = None,
           city: Annotated[Union[str, None], Field(description='A city for location-based searches (e.g., New York).')] = None,
           types: Annotated[Union[str, None], Field(description='Specifies the types of results to include in the search. Available types are -artist -event -festival -venue Multiple types can be specified as a comma-separated list (e.g., artist,event).')] = None,
           page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           sort: Annotated[Union[str, None], Field(description='')] = None,
           latitude: Annotated[Union[int, float, None], Field(description='Coordinates for location-based searches. Use these to find events within a specific radius of a geographical point.')] = None,
           longitude: Annotated[Union[int, float, None], Field(description='Coordinates for location-based searches. Use these to find events within a specific radius of a geographical point.')] = None,
           radius: Annotated[Union[int, float, None], Field(description='The radius (in kilometers) around the specified location (latitude/longitude or city name) to search for events. Defaults to 75 km if not specified.')] = None,
           starts_at: Annotated[Union[str, datetime, None], Field(description='Specifies the starting date and time for the search. Only events happening on or after this date will be included in the results. Use ISO 8601 date format (YYYY-MM-DDTHH:MM:SSZ) or (YYYY-MM-DD)')] = None,
           ends_at: Annotated[Union[str, datetime, None], Field(description='Specifies the ending date and time for the search. Only events happening on or before this date will be included in the results. Use ISO 8601 date format (YYYY-MM-DDTHH:MM:SSZ) or (YYYY-MM-DD)')] = None,
           filter: Annotated[Union[str, None], Field(description='Filters events based on type. Options include physical (for in-person events) and streaming (for online events).')] = None,
           genre: Annotated[Union[str, None], Field(description='Filters by genre. Available genres include - alternative - blues - christian-gospel - classical - country - comedy - electronic - folk - hip-hop - jazz - latin - metal - pop - punk - rnb-soul - reggae - rock If left empty, all genres are included')] = None) -> dict: 
    '''Find events, artists, festivals, and venues based on various filters, including keywords, location, and date range.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'city': city,
        'types': types,
        'page': page,
        'sort': sort,
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius,
        'starts_at': starts_at,
        'ends_at': ends_at,
        'filter': filter,
        'genre': genre,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_bio(artist_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 99')]) -> dict: 
    '''Fetches the biography of a specific artist.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/artist/bio'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artist_id': artist_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_events(artist_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 99')]) -> dict: 
    '''Retrieves upcoming events for a specific artist.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/artist/events'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artist_id': artist_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_similar(artist_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 99')]) -> dict: 
    '''Fetches similar artists to the specified artist.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/artist/similar'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artist_id': artist_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_past(artist_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 99')],
                before: Annotated[Union[str, datetime], Field(description='Filters events to those that occurred before this date.')]) -> dict: 
    '''Retrieves past events for a specific artist.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/artist/past'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artist_id': artist_id,
        'before': before,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def event_infos(event_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 105973572')]) -> dict: 
    '''Fetches details about a specific event.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/event/infos'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venue_infos(venue_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 10091046')]) -> dict: 
    '''Fetches information about a specific venue.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/venue/infos'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'venue_id': venue_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def festival_infos(festival_id: Annotated[Union[int, float], Field(description='The id can be found within the results returned by the /search endpoint Default: 157318')]) -> dict: 
    '''Fetches information about a specific festival.'''
    url = 'https://concerts-artists-events-tracker.p.rapidapi.com/festival/infos'
    headers = {'x-rapidapi-host': 'concerts-artists-events-tracker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'festival_id': festival_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
