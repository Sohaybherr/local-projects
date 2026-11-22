const teamsModel = require("./teams.model");
const countriesModel = require("../countries/countries.model");
const playersModel = require("../players/players.model");
const matchesModel = require("../matches/matches.model");
const competitionsModel = require("../competitions/competitions.model");

function matchIncludesTeam(match, teamId) {
  return String(match.home_team) === String(teamId) || String(match.away_team) === String(teamId);
}

async function getAllTeams(req, res) {
  try {
    const teams = await teamsModel.getAllTeams();
    res.json(teams);
  } catch (error) {
    console.error("Error fetching teams:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getTeamById(req, res) {
  const { id } = req.params;

  try {
    const team = await teamsModel.getTeamById(id);

    if (!team) {
      return res.status(404).json({ error: "Team not found" });
    }

    res.json(team);
  } catch (error) {
    console.error("Error fetching team:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getTeamByApiId(req, res) {
  const { apiId } = req.params;

  try {
    const team = await teamsModel.getTeamByApiId(apiId);

    if (!team) {
      return res.status(404).json({ error: "Team not found" });
    }

    res.json(team);
  } catch (error) {
    console.error("Error fetching team by api id:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getTeamsByCountry(req, res) {
  const { countryId } = req.params;

  try {
    const teams = await teamsModel.getTeamsByCountry(countryId);
    res.json(teams);
  } catch (error) {
    console.error("Error fetching teams by country:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getTeamsByName(req, res) {
  const { name } = req.params;

  try {
    const teams = await teamsModel.getTeamsByName(name);
    res.json(teams);
  } catch (error) {
    console.error("Error fetching teams by name:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getTeamsByCompetitionAndSeason(req, res) {
  const { competitionId, seasonId } = req.params;

  try {
    const teams = await teamsModel.getTeamsByCompetitionAndSeason(competitionId, seasonId);
    res.json(teams);
  } catch (error) {
    console.error("Error fetching teams by competition and season:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getCompetitionsByTeamAndSeason(req, res) {
  const { teamId, seasonId } = req.params;

  try {
    const competitions = await teamsModel.getCompetitionsByTeamAndSeason(teamId, seasonId);
    res.json(competitions);
  } catch (error) {
    console.error("Error fetching competitions by team and season:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getTeamDetails(req, res) {
  const { id } = req.params;

  try {
    const team = await teamsModel.getTeamById(id);

    if (!team) {
      return res.status(404).json({ error: "Team not found" });
    }

    const [country, squad, matches] = await Promise.all([
      team.country_id ? countriesModel.getCountryById(team.country_id) : null,
      playersModel.getPlayersByTeam(id),
      matchesModel.getAllMatches()
    ]);

    const teamMatches = matches
      .filter((match) => matchIncludesTeam(match, id))
      .sort((a, b) => new Date(a.match_date || 0) - new Date(b.match_date || 0));
    const today = new Date();
    const nextMatch = teamMatches.find((match) => match.match_date && new Date(match.match_date) >= today) || null;
    const lastMatches = teamMatches
      .filter((match) => !match.match_date || new Date(match.match_date) < today)
      .slice(-5)
      .reverse();

    const competitionId = teamMatches.find((match) => match.competition_id)?.competition_id;
    const competition = competitionId ? await competitionsModel.getCompetitionById(competitionId) : null;

    res.json({
      team,
      competition,
      country,
      squad,
      nextMatch,
      lastMatches,
      latestTeamNews: []
    });
  } catch (error) {
    console.error("Error fetching team details:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

module.exports = {
  getAllTeams,
  getTeamById,
  getTeamByApiId,
  getTeamsByCountry,
  getTeamsByName,
  getTeamsByCompetitionAndSeason,
  getCompetitionsByTeamAndSeason,
  getTeamDetails
};
