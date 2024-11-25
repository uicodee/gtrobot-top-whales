from apscheduler.jobstores.redis import RedisJobStore

job_stores = {
    "default": RedisJobStore(
        jobs_key="scheduled_gtrobot_jobs",
        run_times_key="scheduled_gtrobot_run_times",
        host="localhost",
        port=6379,
    )
}
