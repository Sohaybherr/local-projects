import { useEffect, useMemo, useState } from "react";
import { getHome } from "../../api/home";
import CountrySection from "../../components/home/CountrySection";
import SearchBar from "../../components/home/SearchBar";

function Home() {
  const [countries, setCountries] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let mounted = true;

    async function loadHome() {
      try {
        setIsLoading(true);
        setError("");

        const response = await getHome();

        console.log(response.data);

        if (mounted) {
          setCountries(response.data);
        }
      } catch (err) {
        console.error(err);

        if (mounted) {
          setError("Unable to load matches.");
        }
      } finally {
        if (mounted) {
          setIsLoading(false);
        }
      }
    }

    loadHome();

    return () => {
      mounted = false;
    };
  }, []);

  const matchCount = useMemo(() => {
    return countries.reduce((total, country) => {
      return (
        total +
        country.competitions.reduce((sum, competition) => {
          return sum + competition.matches.length;
        }, 0)
      );
    }, 0);
  }, [countries]);

  return (
    <section className="home-page">
      <SearchBar />

      <div className="home-page__header">
        <div>
          <p className="eyebrow">Football Dashboard</p>
          <h1>Matches</h1>
        </div>

        <span className="home-page__count">
          {matchCount} matches
        </span>
      </div>

      {isLoading && (
        <p className="state-message">
          Loading...
        </p>
      )}

      {error && (
        <p className="state-message state-message--error">
          {error}
        </p>
      )}

      {!isLoading && !error && countries.length === 0 && (
        <p className="state-message">
          No matches available.
        </p>
      )}

      {!isLoading && !error && countries.length > 0 && (
        <div className="country-list">
          {countries.map((country) => (
            <CountrySection
              key={country.id}
              country={country}
            />
          ))}
        </div>
      )}
    </section>
  );
}

export default Home;