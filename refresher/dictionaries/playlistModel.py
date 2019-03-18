

playlist = {
    "title": "patagonia bus",
    "creator": "Wechuli"
    "songs": [
        {
            "name": "Turn it Off",
            "artists": [
                "Culture Abuse"
            ],
            "album":"Peach",
            "date":"2017-10-31",
            "duration":3.30
        },
        {
            "name": "Eating Hooks - sirusmo remix-Solomun Edit",
            "artists": [
                "Moderat",
                "Siriusmo",
                "Solomun"
            ],
            "album":"Eating Hooks(Siriusmo remix-solomunEdit)",
            "date":"2017-11-06",
            "duration":7.20
        }
    ]
}

print(playlist)
print(playlist['songs'][0])
print(playlist['songs'][1])

print(playlist['songs'][0]['artists'])
print(playlist['songs'][1]['artists'])
