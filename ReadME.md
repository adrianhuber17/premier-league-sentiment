# Premier League Sentiment App ⚽️

## app is currently under construction 🚧

The Premier League sentiment app will allow users to see the premier league sentiment by team on a day to day basis. The app will rank the teams based on their daily sentiment and compare to their current rank on the Premier League Table.
The sentiment analysis is done using NLP (machine learning). The data pipeline consists of daily extractions of the teams' twitter comments, data clean up and organization using python and pandas, run data through NLP machine learning model to get sentiment, and finally sending data to PostgreSQL. PostgreSQL clean data will be used to send to front end as a GET request for plotting.

![](/ReadMeImages/dataPipeline.jpeg)

# Plot Examples:

![](/ReadMeImages/CurrSentimentPlot.png)

# To Do:

- Test data processing and clean up
- Test nlp model and resulting data
- Add Celery
- Add Redis
- Find better way of displaying sentiment plot
- Style dashboard (from web samples)

# Tech Stack...more to come 📚

**Client:** ReactJS, JavaScript, Chart.js

**Server:** Python, Flask, SQLAlchemy, Pandas

**Server:** PostgreSQL

**Other:** Docker, AWS
