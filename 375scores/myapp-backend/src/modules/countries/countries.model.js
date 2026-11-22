const pool = require("../../config/db");

async function getAllCountries() {
    const result = await pool.query("SELECT * FROM countries");
    return result.rows;
}
async function getCountryById(id) {
    const result = await pool.query("SELECT * FROM countries WHERE id = $1", [id]);
    return result.rows[0];
}
async function getCountryByName(name) {
    const result = await pool.query("SELECT * FROM countries WHERE name = $1", [name]);
    return result.rows[0];
}
module.exports = {
    getAllCountries,
    getCountryById,
    getCountryByName
};