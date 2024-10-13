const { Queue } = require('kue');

const jobQueue = 'push_notification_code_3';

const createPushNotificationsJobs = (jobs, queue = new Queue()) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((jobData) => {
    let jobId;
    const job = queue.create(jobQueue, jobData);
    job.on('complete', () => {
      console.log(`Notification job ${jobId} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${jobId} failed: ${err}`);
    });

    job.on('progress', (progress, data) => {
      console.log(`Notification job ${jobId} ${progress}% complete`);
    });

    job.save((err) => {
      if (!err) {
        jobId = job.id;
        console.log(`Notification job created: ${jobId}`);
      }
    });
  });
};

module.exports = createPushNotificationsJobs;
