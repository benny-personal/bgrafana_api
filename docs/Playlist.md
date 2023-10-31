# Playlist

Playlist model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**interval** | **str** | Interval sets the time between switching views in a playlist. FIXME: Is this based on a standardized format or what options are available? Can datemath be used? | [optional] 
**name** | **str** | Name of the playlist. | [optional] 
**uid** | **str** | Unique playlist identifier. Generated on creation, either by the creator of the playlist of by the application. | [optional] 

## Example

```python
from bgrafana_api.models.playlist import Playlist

# TODO update the JSON string below
json = "{}"
# create an instance of Playlist from a JSON string
playlist_instance = Playlist.from_json(json)
# print the JSON string representation of the object
print Playlist.to_json()

# convert the object into a dict
playlist_dict = playlist_instance.to_dict()
# create an instance of Playlist from a dict
playlist_form_dict = playlist.from_dict(playlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


