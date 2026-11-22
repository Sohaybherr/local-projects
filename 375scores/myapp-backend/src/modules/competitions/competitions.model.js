const pool = require('../../config/db');

async function getAllCompetitions() {
  const query = 'SELECT * FROM competitions';
  const result = await pool.query(query);
  return result.rows;
}

async function getCompetitionById(id) {
  const query = 'SELECT * FROM competitions WHERE id = $1';
  const result = await pool.query(query, [id]);
  return result.rows[0];
}

async function getCompetitionByCountry(country) {
  const query = 'SELECT * FROM competitions WHERE country = $1';
  const result = await pool.query(query, [country]);
  return result.rows;
}

async function getCompetitionType(id) {
  const query = 'SELECT type FROM competitions WHERE id = $1';
  const result = await pool.query(query, [id]);
  return result.rows[0];
}

async function getCompetitionSeasons(competitionId) {
  const query = `
    SELECT DISTINCT seasons.*
    FROM seasons
    INNER JOIN team_competitions
      ON team_competitions.season_id = seasons.id
    WHERE team_competitions.competition_id = $1
    ORDER BY seasons.id DESC
  `;
  const result = await pool.query(query, [competitionId]);
  return result.rows;
}


module.exports = {
  getAllCompetitions,
  getCompetitionById,
  getCompetitionByCountry,
  getCompetitionType,
  getCompetitionSeasons
};
