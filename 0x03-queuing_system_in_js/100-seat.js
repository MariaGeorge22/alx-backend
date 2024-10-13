import { createQueue } from 'kue';
import { createClient } from 'redis';
import { promisify } from 'util';

const express = require('express');

const queue = createQueue();
const redis = createClient();
const availableSeats = 50;
const key = 'available_seats';
const jobTitle = 'reserve_seat';

let reservationEnabled = true;

const reserveSeat = (number) => {
  redis.set(key, number);
};

const getCurrentAvailableSeats = async () => {
  return await promisify(redis.get).bind(redis)(key);
};

const app = express();

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.status(403).send({ status: 'Reservation are blocked' });
  }
  const job = queue.create(jobTitle);
  let jobId;
  job.on('complete', () => {
    console.log(`Seat reservation job ${jobId} completed`);
  });
  job.on('failed', (err) => {
    console.err(`Seat reservation job ${jobId} failed: ${err}`);
  });
  job.save((err) => {
    if (err) {
      return res.status(500).send({ status: 'Reservation failed' });
    }
    jobId = job.id;
    res.send({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  queue.process(jobTitle, async (job, done) => {
    const availableSeats = parseInt(await getCurrentAvailableSeats());
    if (availableSeats <= 0) {
      return done(new Error('Not enough seats available'));
    }
    reserveSeat(availableSeats - 1);
    if (availableSeats - 1 === 0) {
      reservationEnabled = false;
    }
    done();
  });
  res.send({ status: 'Queue processing' });
});

app.listen(1245, () => {
  reserveSeat(availableSeats);
  console.log('server is running');
});
