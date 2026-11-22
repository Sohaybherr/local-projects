const matchesModel = require("../matches/matches.model");
const competitionsModel = require("../competitions/competitions.model");
const countriesModel = require("../countries/countries.model");

async function getHome(req, res) {
  try {
    const [matches, competitions, countries] = await Promise.all([
      matchesModel.getAllMatches(),
      competitionsModel.getAllCompetitions(),
      countriesModel.getAllCountries(),
    ]);

    // Countries Map
    const countriesMap = new Map();

    countries.forEach((country) => {
      countriesMap.set(String(country.id), {
        id: country.id,
        name: country.name,
        code: country.code,
        flag: country.flag,
        competitions: [],
      });
    });

    // Competitions Map
    const competitionsMap = new Map();

    competitions.forEach((competition) => {
      const competitionObject = {
        id: competition.id,
        name: competition.name,
        logo: competition.logo,
        matches: [],
      };

      competitionsMap.set(String(competition.id), competitionObject);

      const country = countriesMap.get(String(competition.country_id));

      if (country) {
        country.competitions.push(competitionObject);
      }
    });

    // Add Matches
    matches.forEach((match) => {
      const competition = competitionsMap.get(
        String(match.competition_id)
      );

      if (competition) {
        competition.matches.push(match);
      }
    });

    // Remove empty competitions
    const response = Array.from(countriesMap.values())
      .map((country) => ({
        ...country,
        competitions: country.competitions.filter(
          (competition) => competition.matches.length > 0
        ),
      }))
      .filter((country) => country.competitions.length > 0);

    res.json(response);
  } catch (err) {
    console.error(err);
    res.status(500).json({
      message: "Internal Server Error",
    });
  }
}

module.exports = {
  getHome,
};