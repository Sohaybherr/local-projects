import CompetitionSection from './CompetitionSection'

function CountrySection({ country }) {
  return (
    <section className="country-section">
      <header className="country-section__header">
        <h2>{country.name}</h2>
      </header>

      <div className="competition-list">
        {country.competitions.map((competition) => (
          <CompetitionSection
            key={competition.id ?? competition.name}
            competition={competition}
          />
        ))}
      </div>
    </section>
  )
}

export default CountrySection
