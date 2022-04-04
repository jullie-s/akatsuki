import requests
import json


def postInstaVPB():

    image_location_1 = 'https://github.com/jullie-s/akatsuki/blob/main/Screenshot%202022-04-03%20at%2015-15-53%20Historical%20Sites.jpg?raw=true'.format('Screenshot 2022-04-03 at 15-15-53 Historical Sites.jpg')

    post_url = 'https://graph.facebook.com/v13.0/17841452251535696/media?caption=I%20am%20a%20bot%21%20This%20is%20a%20test%20' \
        'made%20by%20Team%20Akatsuki%21&access_token=EAAHao1ElHaMBAO0YVQtpZCYcOS55BpMPeIaqZAuE0aJhEdEDW6iWmIr7DgotsKyeZAS' \
        'siqMubmWH0QprtFYhcSdQCGVqOcBIQZBX2YcLyXrCikHIV8dD2PgrQkzBvXxHkHBJZCvvIGR0Y9EZAGZAHfvB8ZClOWBO53vfaUiFXWd08G0YWz' \
        '2SUMxS&image_url=https://github.com/jullie-s/akatsuki/blob/main/Screenshot%202022-04-03%20at%2015-15-53%20Historical%20' \
        'Sites.jpg?raw=true'.format(103894095625044)

    payload = {
     'image_url': image_location_1,
     'access_token': 'EAAHao1ElHaMBAO0YVQtpZCYcOS55BpMPeIaqZAuE0aJhEdEDW6iWmIr7DgotsKyeZASsiqMubmWH0QprtFYhcSdQCGVqOcBIQ'
     'ZBX2YcLyXrCikHIV8dD2PgrQkzBvXxHkHBJZCvvIGR0Y9EZAGZAHfvB8ZClOWBO53vfaUiFXWd08G0YWz2SUMxSuser_access_token',
     'caption': 'I am a bot! This is a test made by Team Akatsuki!'

    }

    r = requests.post(post_url, data=payload)
    print(r.text)

    result = json. loads(r.text)

    if 'id' in result:
        creation_id = result['id']

        second_url = 'https://graph.facebook.com/v13.0/17841452251535696/media_publish?creation_id=17930729396301662' \
            '&access_token=EAAHao1ElHaMBAO0YVQtpZCYcOS55BpMPeIaqZAuE0aJhEdEDW6iWmIr7DgotsKyeZASsiqMubmWH0QprtFYhcSdQCGVq' \
            'OcBIQZBX2YcLyXrCikHIV8dD2PgrQkzBvXxHkHBJZCvvIGR0Y9EZAGZAHfvB8ZClOWBO53vfaUiFXWd08G0YWz2SUMxS'.format(103894095625044)
        second_payload = {
            'creation_id': creation_id,
            'access_token': 'EAAHao1ElHaMBAO0YVQtpZCYcOS55BpMPeIaqZAuE0aJhEdEDW6iWmIr7DgotsKyeZASsiqMubmWH0QprtFYhcSdQCGVqOcBIQZB'
            'X2YcLyXrCikHIV8dD2PgrQkzBvXxHkHBJZCvvIGR0Y9EZAGZAHfvB8ZClOWBO53vfaUiFXWd08G0YWz2SUMxS'
        }
        r = requests.post(second_url, data=second_payload)
        print('------Just posted to instagram-----')
        print(r.text)

    else:
        print('HOUSTON we have a problem')



