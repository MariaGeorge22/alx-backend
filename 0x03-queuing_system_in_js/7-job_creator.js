import { createQueue } from 'kue';

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const jobTitle = 'push_notification_code_2';

jobs.forEach(data => {
  const job = queue.create(jobTitle, data);

  let jobId;
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
