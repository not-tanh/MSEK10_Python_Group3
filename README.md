# Installation

`pip install -r requirements
`
# Run app
`uvicorn main:app --reload`

`--reload` is the option to reload the app automatically when change codes. You can drop reload option if you don't need it.<br>


# Run crawler

You need to download chrome driver to run crawler. Download link: https://chromedriver.chromium.org/home <br>

`python selenium_crawler.py --url <website_url> --driver <chrome_driver_path>`
