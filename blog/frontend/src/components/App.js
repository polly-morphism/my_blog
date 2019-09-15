import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";

const App = () => (
  <DataProvider endpoint="blogposts/"
                render={data => <div >{JSON.stringify(data)}</div>} />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
