import React from "react";
import ReactDOM from "react-dom";

const Post = ({match}) => (
    <p>PostId:{match.params.id}</p>
);

export default Post
