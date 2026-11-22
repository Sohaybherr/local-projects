const { Pool } = require("pg");

// Uses standard PGHOST, PGPORT, PGUSER, PGPASSWORD and PGDATABASE variables.
const pool = new Pool();
module.exports = pool;
