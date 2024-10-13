import { createClient } from 'redis';
import { promisify } from 'util';

const express = require('express');

const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
];

const getItemById = (itemId) => listProducts.find((item) => item.Id === itemId);

const redisClient = createClient();

const reserveStockById = (itemId, stock) => {
  redisClient.set(itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  return await promisify(redisClient.get).bind(redisClient)(itemId);
};

const app = express();

app.get('/list_products', (req, res, next) => {
  res.send(listProducts);
});

app.get('/list_products/:itemId', async (req, res, next) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  if (!item) {
    return res.status(404).send({ status: 'Product not found' });
  }
  const reservedQuantity = parseInt(await getCurrentReservedStockById(itemId));
  const currentQuantity = item.stock - reservedQuantity;
  const initialAvailableQuantity = item.stock;
  const returnedItem = { ...item, currentQuantity, initialAvailableQuantity };
  delete returnedItem.stock;
  res.send(returnedItem);
});
app.get('/reserve_product/:itemId', async (req, res, next) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  if (!item) {
    return res.status(404).send({ status: 'Product not found' });
  }
  const reservedQuantity = parseInt(await getCurrentReservedStockById(itemId));
  const currentQuantity = item.stock - reservedQuantity;
  if (currentQuantity <= 0) {
    return res.status(400).send({ status: 'Not enough stock available', itemId });
  }
  reserveStockById(itemId, reservedQuantity + 1);
  res.send({ status: 'Reservation confirmed', itemId });
});

app.listen(1245, () => {
  console.log('server is running');
});
