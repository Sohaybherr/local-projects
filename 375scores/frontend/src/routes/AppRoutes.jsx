import { Route, Routes } from 'react-router-dom'
import MainLayout from '../layouts/MainLayout'
import Home from '../pages/Home/Home'
import Team from '../pages/Team/Team'
import Player from '../pages/Player/Player'
import Competition from '../pages/Competition/Competition'
import Match from '../pages/Match/Match'
import News from '../pages/News/News'
import NewsDetails from '../pages/News/NewsDetails'
import Search from '../pages/Search/Search'
import Profile from '../pages/Profile/Profile'
import NotFound from '../pages/NotFound/NotFound'

function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route index element={<Home />} />
        <Route path="teams/:id" element={<Team />} />
        <Route path="players/:id" element={<Player />} />
        <Route path="competitions/:id" element={<Competition />} />
        <Route path="matches/:id" element={<Match />} />
        <Route path="news" element={<News />} />
        <Route path="news/:id" element={<NewsDetails />} />
        <Route path="search" element={<Search />} />
        <Route path="profile" element={<Profile />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}

export default AppRoutes
