# Facebook Scraper API

Use Flask API to wrap Facebook data. Grab the wapper of Facebook public pages without an API key. (Currently working 2021)

#### Setup

Before using this scraper API, please export the cookies of your Facebook account and save them to `/tmp/cookies.text`

**Cookies**

The path to a file containing cookies in Netscape or JSON format. You can extract cookies from your browser after logging into Facebook with an extension like [EditThisCookie (Chrome)](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) or [Cookie Quick Manager (Firefox)](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/). Make sure that you include both the c_user cookie and the xs cookie, you will get an InvalidCookies exception if you don't.

#### Start and run the script locally

```shell
export FLASK_ENV=development
export FLASK_APP=src/index.py

# now we just need to ask flask to run
flask run
```

#### Facebook API URL

- Get organization profile (http://127.0.0.1:5000/facebook/organization/ekohe.co)
- Get person profile (http://127.0.0.1:5000/facebook/person/encoreshao)