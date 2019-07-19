""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
import random

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
                                    delimit_by_numbers=True,
                                    max_followers=700,
                                    min_followers=30,
                                    min_following=60,
                                    max_following=1200)
    
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(57, 200),
                               peak_comments=(21, 182),
                                peak_follows=(20, 100),
                                 peak_unfollows=(20, 100),
                                  peak_server_calls=(None, 4700))
    
    session.set_skip_users(skip_private=False,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100,
                       skip_business=False,
		               skip_non_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[])

    # activity
    acc = ['thefaeryforest','blessedbranches','natalia_lefay']
    
    session.follow_likers(acc, photos_grab_amount = random.randint(2,5), follow_likers_per_photo = random.randint(7,15), randomize=True, sleep_delay=600, interact=False)
