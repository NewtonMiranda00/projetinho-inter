import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Header.module.css';

export function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>
        <img src="/favicon.png" alt="Logo I-Graphic" height={90} />
        <h1>I-Graphic</h1>
      </div>
      <nav>
        <li>
          <Link className={styles.link} to={'/'}>
            Início
            <span />
          </Link>
        </li>
        <li>
          <Link className={styles.link} to={'/team'}>
            Equipe
            <span />s
          </Link>
        </li>
      </nav>
    </header>
  );
}
