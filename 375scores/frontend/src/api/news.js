import api from './api'

export const getNews = () => api.get('/news')
export const getNewsById = (id) => api.get(`/news/${id}`)
