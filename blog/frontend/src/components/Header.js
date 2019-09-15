import React from "react";
import ReactDOM from "react-dom";

const Header = () => (
    <header>
        <h1>
            Tech Student 101
        </h1>
        <ul>
            <li><a href="/blog/list/">Home</a></li>
            <li><a href="/blog/create/">Create Post!</a></li>
        </ul>
    </header>
);

export default Header
