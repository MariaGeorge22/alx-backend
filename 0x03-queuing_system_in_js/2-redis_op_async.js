import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const getPromise = promisify(client.get).bind(client);
  try {
    const result = await getPromise(schoolName);
    if (result) {
      console.log(result);
    }
  } catch (err) {
    console.error(err);
  }
};

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};

main();
