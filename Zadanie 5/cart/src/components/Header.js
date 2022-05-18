import React from 'react';


export default function Header(props) {
    return (
        <header className="row block center">
            <div><a href='#/'>
                <h1> Projekt React Usługi</h1>
            </a>
            </div>
            <div><a href='#/cart'>Koszyk{' '}{props.countCartItems ? (<button className="badge">{props.countCartItems}</button>
          ) : (
            ''
          )}</a>{' '} <a href='#/signin'>Logowanie</a>
            </div>
        </header>
    );
}