const playersModel = require("./players.model");
const teamsModel = require("../teams/teams.model");
const countriesModel = require("../countries/countries.model");
const matchesModel = require("../matches/matches.model");

async function getAllPlayers(req, res) {
  try {
    const players = await playersModel.getAllPlayers();
    res.json(players);
  } catch (error) {
    console.error("Error fetching players:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayerById(req, res) {
  const { id } = req.params;

  try {
    const player = await playersModel.getPlayerById(id);

    if (!player) {
      return res.status(404).json({ error: "Player not found" });
    }

    res.json(player);
  } catch (error) {
    console.error("Error fetching player:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayerByApiId(req, res) {
  const { apiId } = req.params;

  try {
    const player = await playersModel.getPlayerByApiId(apiId);

    if (!player) {
      return res.status(404).json({ error: "Player not found" });
    }

    res.json(player);
  } catch (error) {
    console.error("Error fetching player by api id:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayersByCountry(req, res) {
  const { countryId } = req.params;

  try {
    const players = await playersModel.getPlayersByCountry(countryId);
    res.json(players);
  } catch (error) {
    console.error("Error fetching players by country:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayersByTeam(req, res) {
  const { teamId } = req.params;

  try {
    const players = await playersModel.getPlayersByTeam(teamId);
    res.json(players);
  } catch (error) {
    console.error("Error fetching players by team:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayersByPosition(req, res) {
  const { position } = req.params;

  try {
    const players = await playersModel.getPlayersByPosition(position);
    res.json(players);
  } catch (error) {
    console.error("Error fetching players by position:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayersByName(req, res) {
  const { name } = req.params;

  try {
    const players = await playersModel.getPlayersByName(name);
    res.json(players);
  } catch (error) {
    console.error("Error fetching players by name:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getPlayerDetails(req, res) {
  const { id } = req.params;

  try {
    const player = await playersModel.getPlayerById(id);

    if (!player) {
      return res.status(404).json({ error: "Player not found" });
    }

    const [currentTeam, country, matches] = await Promise.all([
      player.current_team_id ? teamsModel.getTeamById(player.current_team_id) : null,
      player.country_id ? countriesModel.getCountryById(player.country_id) : null,
      matchesModel.getAllMatches()
    ]);

    const today = new Date();
    const nextMatch = player.current_team_id
      ? matches
          .filter((match) =>
            String(match.home_team) === String(player.current_team_id) ||
            String(match.away_team) === String(player.current_team_id)
          )
          .sort((a, b) => new Date(a.match_date || 0) - new Date(b.match_date || 0))
          .find((match) => match.match_date && new Date(match.match_date) >= today) || null
      : null;

    res.json({
      player,
      currentTeam,
      country,
      statistics: [],
      transferHistory: [],
      nextMatch
    });
  } catch (error) {
    console.error("Error fetching player details:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

module.exports = {
  getAllPlayers,
  getPlayerById,
  getPlayerByApiId,
  getPlayersByCountry,
  getPlayersByTeam,
  getPlayersByPosition,
  getPlayersByName,
  getPlayerDetails
};
