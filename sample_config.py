HEROKU = False  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 7159660
    API_HASH = "e1d5bfd2975078a56213605ce0d7f550"
    ARQ_API_KEY = "BVLSHK-UDVBNB-QQHOPO-OALHMP-ARQ"
    CHAT_ID = -1001457893155
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    SESSION_STRING = "AQAAjg_nngvg5JUHI_tIjTIFl74Vgexp4PmWGP7iu9SwbWBjTlRzVXdpLyQtooGsI3NXl50JstWuu9VRr8oJT7Keh2giGTwsweIgPt-8-pZL1ik6sXNXatDbXIOlNe3mpMrPwqTiqwU9UgRXtZiuOsqUI5F86aIagXl03Pw-opGA6PzXd3mjFa-9sE_5kxI5DDtAvPRZ0Dshth744zKE0yi8r1yHfavLad7p-z27qj64K2kQZklTjbkjjRip3dR8vJZBqBqXHJpZaYG5K-pLrR0ZFh0Mx8UCx7aaaDL-Y_cdBcLqk3t8DbQGJZsqobjkpOxjTsU7fYzXGTOtSf5Bm1YvdCqCJAA"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
