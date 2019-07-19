""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'witchfair'  # <- enter username here
insta_password = 'Abhimanyu.anuj!1'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.15,
                                    delimit_by_numbers=True,
                                    max_followers=500,
                                    min_followers=25,
                                    min_following=80,
                                    max_following=1200)
    
    
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(50, 400),
                               peak_comments=(21, 150),
                                peak_follows=(2, 150),
                                 peak_unfollows=(35, 402),
                                  peak_server_calls=(None, 4700))



    # activity
    
    session.follow_likers(['crystals_healing'], photos_grab_amount = 2, follow_likers_per_photo = 10, randomize=True, sleep_delay=600, interact=False)

    
