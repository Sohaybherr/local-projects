import api from './api'

export const getMatches = () => api.get('/matches')
export const getMatchById = (id) => api.get(`/matches/${id}`)
