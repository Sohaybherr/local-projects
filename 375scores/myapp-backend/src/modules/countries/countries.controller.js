const countriesModel = require("./countries.model");

async function getAllCountries(req, res) {
    try {
        const countries = await countriesModel.getAllCountries();
        res.json(countries);
    } catch (error) {
        console.error("Error fetching countries:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }   
}
async function getCountryById(req, res) {
    const { id } = req.params;
    try {
        const country = await countriesModel.getCountryById(id);
        if (!country) {
            return res.status(404).json({ error: "Country not found" });
        }
        res.json(country);
    } catch (error) {
        console.error("Error fetching country:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }
}
async function getCountryByName(req, res) {
    const { name } = req.params;
    try {
        const country = await countriesModel.getCountryByName(name);
        if (!country) {
            return res.status(404).json({ error: "Country not found" });
        }
        res.json(country);
    } catch (error) {
        console.error("Error fetching country:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }
}
module.exports = {
    getAllCountries,
    getCountryById,
    getCountryByName
};