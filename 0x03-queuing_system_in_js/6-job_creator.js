import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '0123456789',
  message: 'Testing'
};

const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});
