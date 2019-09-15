import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import "../css/blog.css"

import { Post, Posts } from '../pages'
import Header from './Header'

const App = () => (
    <Router>
        <Header/>
        <div className="container">
            <Switch>
                <Route path="/" exact component={Posts} />
                <Route path="/:id" component={Post} />
            </Switch>
        </div>
    </Router>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;


// <DataProvider
//     endpoint="blogposts/"
//     render={data => <div >{JSON.stringify(data)}</div>}
// />
