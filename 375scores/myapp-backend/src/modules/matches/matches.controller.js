const matchesModel = require("./matches.model");
const teamsModel = require("../teams/teams.model");

async function getAllMatches(req, res) {
  try {
    const matches = await matchesModel.getAllMatches();
    res.json(matches);
  } catch (error) {
    console.error("Error fetching matches:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getMatchById(req, res) {
  const { id } = req.params;

  try {
    const match = await matchesModel.getMatchById(id);

    if (!match) {
      return res.status(404).json({ error: "Match not found" });
    }

    res.json(match);
  } catch (error) {
    console.error("Error fetching match:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getMatchesByCompetitionAndSeason(req, res) {
  const { competitionId, seasonId } = req.params;

  try {
    const matches = await matchesModel.getMatchesByCompetitionAndSeason(competitionId, seasonId);
    res.json(matches);
  } catch (error) {
    console.error("Error fetching matches by competition and season:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getMatchesByTeamAndSeasonAndCompetition(req, res) {
  const { teamId, seasonId, competitionId } = req.params;

  try {
    const matches = await matchesModel.getMatchesByTeamAndSeasonAndCompetition(
      teamId,
      seasonId,
      competitionId
    );
    res.json(matches);
  } catch (error) {
    console.error("Error fetching matches by team, season, and competition:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getMatchesByDateRangeAndCompetition(req, res) {
  const { competitionId } = req.params;
  const { startDate, endDate } = req.query;

  if (!startDate || !endDate) {
    return res.status(400).json({ error: "startDate and endDate are required" });
  }

  try {
    const matches = await matchesModel.getMatchesByDateRangeAndCompetition(
      startDate,
      endDate,
      competitionId
    );
    res.json(matches);
  } catch (error) {
    console.error("Error fetching matches by date range and competition:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getMatchDetails(req, res) {
  const { id } = req.params;

  try {
    const fixture = await matchesModel.getMatchById(id);

    if (!fixture) {
      return res.status(404).json({ error: "Match not found" });
    }

    const [homeTeam, awayTeam] = await Promise.all([
      fixture.home_team ? teamsModel.getTeamById(fixture.home_team) : null,
      fixture.away_team ? teamsModel.getTeamById(fixture.away_team) : null
    ]);

    res.json({
      fixture,
      homeTeam,
      awayTeam,
      score: {
        home: fixture.home_score ?? fixture.home_goals ?? null,
        away: fixture.away_score ?? fixture.away_goals ?? null
      },
      statistics: [],
      events: [],
      lineups: []
    });
  } catch (error) {
    console.error("Error fetching match details:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

module.exports = {
  getAllMatches,
  getMatchById,
  getMatchesByCompetitionAndSeason,
  getMatchesByTeamAndSeasonAndCompetition,
  getMatchesByDateRangeAndCompetition,
  getMatchDetails
};
