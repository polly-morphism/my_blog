import React from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";
import MainLeft from "../components/MainPage/MainLeft"
import MainRight from "../components/MainPage/MainRight"

const Main = ({match}) => (
    <div className="main-page">
        <MainLeft/>
        <MainRight/>
    </div>
);

export default Main
