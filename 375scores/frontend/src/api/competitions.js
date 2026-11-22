import api from './api'

export const getCompetitions = () => api.get('/competitions')
export const getCompetitionById = (id) => api.get(`/competitions/${id}`)
