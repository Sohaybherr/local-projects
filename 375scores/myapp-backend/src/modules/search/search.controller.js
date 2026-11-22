const teamsModel = require("../teams/teams.model");
const playersModel = require("../players/players.model");
const competitionsModel = require("../competitions/competitions.model");

async function search(req, res) {
  const { q } = req.query;

  if (!q) {
    return res.status(400).json({ error: "q is required" });
  }

  try {
    const [teams, players, competitions] = await Promise.all([
      teamsModel.getTeamsByName(q),
      playersModel.getPlayersByName(q),
      competitionsModel.getAllCompetitions()
    ]);

    const normalizedQuery = q.toLowerCase();

    res.json({
      teams,
      players,
      competitions: competitions.filter((competition) =>
        String(competition.name || "").toLowerCase().includes(normalizedQuery)
      )
    });
  } catch (error) {
    console.error("Error searching:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

module.exports = {
  search
};
