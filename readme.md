# Demonstration of the Watson Speech to Text service

1. Clone this repository
1. `pip install watson_developer_cloud dotenv pyaudio`<sup>1</sup>
1. Create Bluemix account: https://console.bluemix.net/
1. In your Bluemix dashboard, click *Create Service*
1. Select *Speech to text* -> *Create*
1. Click *Service Credentials* -> *View credentials*, copy username and password to `.env`<sup>2</sup> file
1. run `python main.py`

<sup>1</sup> OS X, install portaudio first: http://macappstore.org/portaudio/

<sup>2</sup> Rename the `.env.example` file to `.env`
