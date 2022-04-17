import React, { Component } from 'react';
import './test.css';

function Test() {
    return (
        <div className="App">
            <header className="App-header">
                {/* <img src={logo} className="App-logo" alt="logo" /> */}
                <h1>Eh, tu! ¿Qué haces aquí?</h1>
                <h2>¿Qué haces aquí?</h2>
                <h3>¿Qué haces aquí?</h3>
                <h4>¿Qué haces aquí?</h4>
                <h5>¿Qué haces aquí?</h5>
                <h6>Creado por Daniel Sateler y Sebastian Diaz</h6>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default Test;
