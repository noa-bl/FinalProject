db.createUser({
    user: "myUserAdmin",
    pwd: "changeme",
    roles: [
      {
        role: "readWrite",
        db: "admin"
      }
    ]
  });
  