import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';

const queue = createQueue();

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('Testing createPushNotifications', () => {
  it('should display error if jobs isn\'t an array', () => {
    expect(() => createPushNotificationsJobs(0, queue)).to.throw('Jobs is not an array');
  });
  it('should create 2 jobs', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.be.equal(2);
  });
});
