function SearchBar() {
  return (
    <div className="home-search" role="search">
      <label className="home-search__label" htmlFor="home-search">
        Search
      </label>
      <input
        id="home-search"
        className="home-search__input"
        type="search"
        placeholder="Search teams, competitions, or matches"
        disabled
      />
    </div>
  )
}

export default SearchBar
