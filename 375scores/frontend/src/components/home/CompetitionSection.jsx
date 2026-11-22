import MatchCard from './MatchCard'

function CompetitionSection({ competition }) {
  return (
    <section className="competition-section">
      <header className="competition-section__header">
        {competition.logo && (
          <img
            className="competition-section__logo"
            src={competition.logo}
            alt=""
          />
        )}
        <div>
          <h3>{competition.name}</h3>
          <p>{competition.matches.length} matches</p>
        </div>
      </header>

      <div className="match-list">
        {competition.matches.map((match) => (
          <MatchCard key={match.id} match={match} />
        ))}
      </div>
    </section>
  )
}

export default CompetitionSection
