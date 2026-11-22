const newsModel = require("./news.model");

async function getAllNews(req, res) {
  try {
    const news = await newsModel.getAllNews();
    res.json(news);
  } catch (error) {
    console.error("Error fetching news:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getLatestNews(req, res) {
  const limit = Number(req.query.limit) || 10;

  try {
    const news = await newsModel.getLatestNews(limit);
    res.json(news);
  } catch (error) {
    console.error("Error fetching latest news:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function getNewsById(req, res) {
  const { id } = req.params;

  try {
    const news = await newsModel.getNewsById(id);

    if (!news) {
      return res.status(404).json({ error: "News not found" });
    }

    res.json(news);
  } catch (error) {
    console.error("Error fetching news:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function createNews(req, res) {
  const { title, content, image, publishedAt } = req.body;

  if (!title || !content) {
    return res.status(400).json({ error: "title and content are required" });
  }

  try {
    const news = await newsModel.createNews({ title, content, image, publishedAt });
    res.status(201).json(news);
  } catch (error) {
    console.error("Error creating news:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function updateNews(req, res) {
  const { id } = req.params;
  const { title, content, image, publishedAt } = req.body;

  try {
    const news = await newsModel.updateNews(id, { title, content, image, publishedAt });

    if (!news) {
      return res.status(404).json({ error: "News not found" });
    }

    res.json(news);
  } catch (error) {
    console.error("Error updating news:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

async function deleteNews(req, res) {
  const { id } = req.params;

  try {
    const news = await newsModel.deleteNews(id);

    if (!news) {
      return res.status(404).json({ error: "News not found" });
    }

    res.json(news);
  } catch (error) {
    console.error("Error deleting news:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

module.exports = {
  getAllNews,
  getLatestNews,
  getNewsById,
  createNews,
  updateNews,
  deleteNews
};
