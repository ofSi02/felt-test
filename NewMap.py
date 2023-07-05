import requests
NewMap = requests.post(
    f"https://felt.com/api/v1/maps", 
    headers={
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
    },
    json={ "title": "title", "basemap":"satellite", "layer_urls":["https://gis.apfo.usda.gov/arcgis/rest/services/NAIP/USDA_CONUS_PRIME/ImageServer/tile/{z}/{y}/{x}"]}, 
)