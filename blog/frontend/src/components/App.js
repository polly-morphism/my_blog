import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import "../css/blog.css"

import { Post, Posts, Main } from '../pages'
// import Header from './Header'

const App = () => (
    <Router>
            <Switch>
                <Route path="/posts" exact component={Posts} />
                <Route path="/" exact component={Main} />
                <Route path="/:id" component={Post} />
            </Switch>
    </Router>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;


// <DataProvider
//     endpoint="blogposts/"
//     render={data => <div >{JSON.stringify(data)}</div>}
// />
