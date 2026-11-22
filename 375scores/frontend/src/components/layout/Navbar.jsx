function Navbar() {
  return (
    <header className="navbar">
      <a className="navbar__brand" href="/">
        375Scores
      </a>
      <nav className="navbar__nav" aria-label="Primary navigation">
        <a href="/">Matches</a>
        <a href="/news">News</a>
        <a href="/search">Search</a>
      </nav>
    </header>
  )
}

export default Navbar
