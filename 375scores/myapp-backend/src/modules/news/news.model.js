const pool = require("../../config/db");

async function getAllNews() {
  const result = await pool.query("SELECT * FROM news ORDER BY published_at DESC");
  return result.rows;
}

async function getLatestNews(limit = 10) {
  const result = await pool.query("SELECT * FROM news ORDER BY published_at DESC LIMIT $1", [limit]);
  return result.rows;
}

async function getNewsById(id) {
  const result = await pool.query("SELECT * FROM news WHERE id = $1", [id]);
  return result.rows[0];
}

async function createNews(news) {
  const { title, content, image, publishedAt } = news;
  const query = `
    INSERT INTO news (title, content, image, published_at)
    VALUES ($1, $2, $3, COALESCE($4, CURRENT_TIMESTAMP))
    RETURNING *
  `;
  const result = await pool.query(query, [title, content, image || null, publishedAt || null]);
  return result.rows[0];
}

async function updateNews(id, news) {
  const { title, content, image, publishedAt } = news;
  const query = `
    UPDATE news
    SET
      title = COALESCE($1, title),
      content = COALESCE($2, content),
      image = COALESCE($3, image),
      published_at = COALESCE($4, published_at)
    WHERE id = $5
    RETURNING *
  `;
  const result = await pool.query(query, [title, content, image, publishedAt, id]);
  return result.rows[0];
}

async function deleteNews(id) {
  const result = await pool.query("DELETE FROM news WHERE id = $1 RETURNING *", [id]);
  return result.rows[0];
}

module.exports = {
  getAllNews,
  getLatestNews,
  getNewsById,
  createNews,
  updateNews,
  deleteNews
};
