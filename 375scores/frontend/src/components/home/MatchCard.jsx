function TeamIdentity({ team }) {
  return (
    <div className="match-card__team">
      {team.logo ? (
        <img className="match-card__logo" src={team.logo} alt="" />
      ) : (
        <span className="match-card__logo match-card__logo--empty">
          {String(team.name).charAt(0).toUpperCase()}
        </span>
      )}
      <span className="match-card__team-name">{team.name}</span>
    </div>
  )
}

function MatchCard({ match }) {
  return (
    <article className="match-card">
      <div className="match-card__meta">
        <span>{match.time}</span>
        <span>{match.status}</span>
      </div>

      <div className="match-card__body">
        <TeamIdentity team={match.homeTeam} />
        <div className="match-card__center">
          {match.score ? <strong>{match.score}</strong> : <span>VS</span>}
        </div>
        <TeamIdentity team={match.awayTeam} />
      </div>
    </article>
  )
}

export default MatchCard
