import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-container">
        <div className="header-brand">
          <h1>💰 Finance Dashboard</h1>
        </div>
        <nav className="header-nav">
          <a href="/" className="nav-link active">Dashboard</a>
        </nav>
      </div>
    </header>
  );
};

export default Header;
