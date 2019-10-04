import React from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";


const MainLeft = ({match}) => (
    <div className="left-side">
        <div className="main-text">
        Welcome
        </div>
        <div className="links-list">
        <Link to="/posts/">
        <li>Posts</li>
        </Link>
        <Link to="/posts/create/">
        <li>Create a post!</li>
        </Link>
        </div>
    </div>
);

export default MainLeft
