# Requirements
`python 3.9`

# Installation
`pip install -r requirements.txt `

# Run app
`uvicorn main:app --reload`

`--reload` is the option to reload the app automatically when change codes. You can drop reload option if you don't need it.<br>

The app will run on port 8000 by default.

# Create fake data
`python data_generator.py n (n is the number of rows you want to create)`

# Run crawler
You need to download chrome driver to run crawler. Download link: https://chromedriver.chromium.org/home <br>

`python selenium_crawler.py --url <website_url> --driver <chrome_driver_path>`

The crawled data will be saved to `output.csv`
