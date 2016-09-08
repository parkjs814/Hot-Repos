import schedule
import time
import github
import sns
import db


def job():
    repos = github.get_hot_repos()
    for repo in repos:
        if not db.has_posted(repo):
            if sns.post(repo):
                db.posted(repo)
            break


def run():
    job()
    schedule.every(5).minutes.do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)