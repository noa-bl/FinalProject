const database = 'Project';
const collectionName = 'Users';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collectionName);

const collection = db.getCollection(collectionName);

const users = [
  {username: "Noa", password: '1123'},
  {username: "Mai", password: '2123'}
];

collection.insertMany(users);
