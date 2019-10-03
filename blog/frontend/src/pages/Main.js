import React from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";

const Main = ({match}) => (
    <div className="main-page">
        <div className="left-side">
            <div className="main-text">
            Text
            </div>
            <div className="links-list">
            Links
            <Link to="/posts/">
            Posts
            </Link>
            </div>
        </div>
        <div className="right-side">

        </div>
    </div>
);

export default Main
