import React from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";
import MainLeft from "../components/MainLeft"
// import MainLeft from "../components/MainRight"

const Main = ({match}) => (
    <div className="main-page">
        <MainLeft/>
        <div className="right-side">
            <img src="https://image.vsco.co/1/5623aa69348fb9312093/58dfca75555d574c2a049bae/1136x1515/vsco_040117.jpg"/>
        </div>
    </div>
);

export default Main
