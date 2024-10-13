import { createClient, print } from 'redis';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

const key = 'HolbertonSchools';
client.hset(key, 'Portland', 50, print);
client.hset(key, 'Seattle', 80, print);
client.hset(key, 'New York', 20, print);
client.hset(key, 'Bogota', 20, print);
client.hset(key, 'Cali', 40, print);
client.hset(key, 'Paris', 2, print);

client.hgetall(key, (err, reply) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(reply);
});
