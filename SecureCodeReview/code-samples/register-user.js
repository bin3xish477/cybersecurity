/*
Does the following code have any vulnerabilities?
*/

const express = require('express');
const User = require('../models/User');
const bcrypt = require('bcrypt');

const router = express.Router();

router.post("/register", async (req, res) => {
  const { full_name, email, passwd } = res.body;
  
  if (!(full_name && email && passwd)) {
    return res.json("missing fields");
  }
  
  try {
    const userExists = await User.findOne({ email: email });
    if (userExists) {
      return res.json({error: "user exists. redirecting to login"});
    }
    
    passwdHash = await bcrypt.hash(passwd, 10);
    const user = await User.create({
      full_name: full_name,
      email: email.toLowerCase(),
      passwd: passwdHash
    });
    
    return res.json({ full_name, email, createdAt: user.createdAt });
    
  } catch (err) {
    return res.json(err);
  }
});

module.exports = router;
