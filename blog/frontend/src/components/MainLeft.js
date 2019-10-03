import React from "react";
import ReactDOM from "react-dom";

const MainLeft = ({match}) => (
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
);

export default MainLeft
