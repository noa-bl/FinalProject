const database = 'Project';
const collectionName = 'Posts';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collectionName);

const collection = db.getCollection(collectionName);

const posts = [
  {username: "Noa", _title:"one",content:"this info noa", likes: '[]'},
  {username: "Mai", _title:"one",content:"this info mai", likes: '[]'},
  {username: "Noa", _title:"two",content:"this info noa2", likes: '[]'}
];

collection.insertMany(posts);